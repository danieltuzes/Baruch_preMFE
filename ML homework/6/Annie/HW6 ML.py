#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('pip', 'install yfinance numpy pandas scikit-learn xgboost matplotlib')


# In[17]:


import datetime
import numpy as np
import pandas as pd
import yfinance as yf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


# In[18]:


def fetch_and_preprocess_data(ticker, start='2015-01-01', end=None):
    if end is None:
        end = datetime.date.today().strftime('%Y-%m-%d')

    # Force only one ticker, no grouping
    df = yf.download(
        ticker,
        start=start,
        end=end,
        progress=False,
        auto_adjust=False,
        group_by="column"  # or omit group_by entirely
    )
    df.dropna(inplace=True)
    
    # If the columns are still a MultiIndex, flatten them:
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    # Now do your computations
    df['Return'] = df['Adj Close'].pct_change()
    df['Volatility_5'] = df['Return'].rolling(window=5).std()
    df['SMA_5'] = df['Adj Close'].rolling(window=5).mean()
    df['SMA_20'] = df['Adj Close'].rolling(window=20).mean()
    
    rolling_std_20 = df['Adj Close'].rolling(window=20).std()
    df['BB_Mid'] = df['SMA_20']
    df['BB_Upper'] = df['BB_Mid'] + 2 * rolling_std_20
    df['BB_Lower'] = df['BB_Mid'] - 2 * rolling_std_20

    # RSI
    def compute_RSI(series, period=14):
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    df['RSI_14'] = compute_RSI(df['Adj Close'], 14)

    df['Volume_5_SMA'] = df['Volume'].rolling(window=5).mean()

    df.dropna(inplace=True)
    return df



# In[19]:


def build_datasets(tickers, start='2015-01-01', end=None, tau=0.005):
    """
    Downloads data for each ticker, computes features, applies label columns,
    and returns combined DataFrames for daily, weekly, monthly.
    """
    all_daily = []
    all_weekly = []
    all_monthly = []

    # We'll define a set of feature columns we want to include in the final dataset
    feature_cols = [
        'Return',
        'Volatility_5',
        'SMA_5',
        'SMA_20',
        'BB_Upper',
        'BB_Mid',
        'BB_Lower',
        'RSI_14',
        'Volume',
        'Volume_5_SMA'
    ]

    for t in tickers:
        df_t = fetch_and_preprocess_data(t, start, end)
        df_t = prepare_label_columns(df_t, tau)

        # For daily
        df_daily = df_t.dropna(subset=['Daily_Labels']).copy()
        df_daily['Ticker'] = t
        daily_subset = df_daily[feature_cols + ['Daily_Labels']]
        all_daily.append(daily_subset)

        # For weekly
        df_weekly = df_t.dropna(subset=['Weekly_Labels']).copy()
        df_weekly['Ticker'] = t
        weekly_subset = df_weekly[feature_cols + ['Weekly_Labels']]
        all_weekly.append(weekly_subset)

        # For monthly
        df_monthly = df_t.dropna(subset=['Monthly_Labels']).copy()
        df_monthly['Ticker'] = t
        monthly_subset = df_monthly[feature_cols + ['Monthly_Labels']]
        all_monthly.append(monthly_subset)

    # Combine all tickers into 3 big dataframes
    df_daily_all = pd.concat(all_daily, axis=0)
    df_weekly_all = pd.concat(all_weekly, axis=0)
    df_monthly_all = pd.concat(all_monthly, axis=0)

    return df_daily_all, df_weekly_all, df_monthly_all, feature_cols


# In[20]:


def train_and_evaluate_classifiers(df, feature_cols, label_col, random_state=42):
    X = df[feature_cols].values
    y_original = df[label_col].values

    # Remap labels:
    #   -1 -> 0  (negative)
    #    0 -> 1  (neutral)
    #   +1 -> 2  (positive)
    label_map = {-1: 0, 0: 1, 1: 2}
    y = np.array([label_map[val] for val in y_original])

    # Now y is in [0, 1, 2], which XGBoost expects for multiclass
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, shuffle=True, random_state=random_state
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        'LogisticRegression': LogisticRegression(
            max_iter=1000,
            multi_class='multinomial',
            random_state=random_state
        ),
        'RandomForest': RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=random_state
        ),
        'XGBClassifier': XGBClassifier(
            n_estimators=100,
            max_depth=5,
            use_label_encoder=False,
            eval_metric='mlogloss',
            random_state=random_state
        )
    }

    trained_models = {}

    for name, model in models.items():
        if name == 'LogisticRegression':
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

        # Print metrics
        acc = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        
        # For a nice classification_report with custom labels:
        target_names = ['Negative', 'Neutral', 'Positive']
        cr = classification_report(y_test, y_pred, digits=3, target_names=target_names)

        print(f"\n=== {name} ===")
        print(f"Accuracy: {acc:.4f}")
        print("Confusion Matrix:\n", cm)
        print("Classification Report:\n", cr)

        trained_models[name] = (model, scaler)

    return trained_models


# In[21]:


tickers = [
    'AAPL',  # Tech
    'MSFT',  # Tech
    'JNJ',   # Healthcare
    'PFE',   # Pharma
    'XOM',   # Energy
    'CVX',   # Energy
    'JPM',   # Financial
    'BAC',   # Financial
    'WMT',   # Consumer Defensive
    'TGT',   # Consumer Defensive
    'HD',    # Consumer Cyclical
    'MCD',   # Restaurant/Retail
    'TSLA',  # Automotive/Tech
    'F',     # Automotive
    'BA',    # Aerospace
    'CAT',   # Industrials
    'IBM',   # Tech
    'AMZN',  # Tech/Retail
    'GOOGL', # Tech
    'META'   # Tech
]

print("Building datasets (daily, weekly, monthly)...")
df_daily_all, df_weekly_all, df_monthly_all, feature_cols = build_datasets(
    tickers,
    start='2015-01-01',
    end=None,      # up to today's date
    tau=0.005      # ±0.5% threshold for neutral
)

print("Datasets built:")
print(f"  Daily:   {df_daily_all.shape[0]} rows")
print(f"  Weekly:  {df_weekly_all.shape[0]} rows")
print(f"  Monthly: {df_monthly_all.shape[0]} rows")

# 6.2: Train & Evaluate for Daily
print("\n===== DAILY PREDICTION =====")
daily_models = train_and_evaluate_classifiers(df_daily_all, feature_cols, 'Daily_Labels')

# 6.3: Train & Evaluate for Weekly
print("\n===== WEEKLY PREDICTION =====")
weekly_models = train_and_evaluate_classifiers(df_weekly_all, feature_cols, 'Weekly_Labels')

# 6.4: Train & Evaluate for Monthly
print("\n===== MONTHLY PREDICTION =====")
monthly_models = train_and_evaluate_classifiers(df_monthly_all, feature_cols, 'Monthly_Labels')

print("\nAll done! Check the accuracy, confusion matrices, and classification reports above.")


# In[ ]:




