"""
stock_classification_2009_2015.py

Script to train a 3-class classifier (-1, 0, +1) on daily forward returns of 21
non-dividend-paying stocks from 2009-01-01 through 2015-11-30, with
features including P/E ratio and rolling averages (5, 20, 90 days) of
returns, volatility, and volume.

Train period: 2009-01-01 to 2014-12-31
Test period:  2015-01-01 to 2015-11-30
"""

from sklearn.model_selection import train_test_split
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

#############################################
# 1. SELECT 21 TICKERS (NON-DIV PAYING)
#############################################

# These are example tickers that (mostly) had no dividend 2009–2015
# and existed in that period. Replace if needed.
tickers = [
    "AMZN", "GOOG", "TSLA", "CRM", "ADBE", "BIIB", "ISRG", "VRTX", "REGN",
    "ILMN", "EBAY", "BIDU", "NFLX", "BKNG", "LULU", "ADSK", "BRK.B", "BMRN",
    "ALGN", "UBER", "EA"
]

start_date = "2009-01-01"
end_date = "2015-11-30"

#############################################
# 2. DOWNLOAD DATA USING YFINANCE
#############################################
# We'll get daily data (Open/High/Low/Close/Adj Close/Volume) for each ticker.

print("Downloading data from yfinance...\n")
data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    auto_adjust=False  # so that we keep 'Adj Close' and can see raw dividends if any
)

# We expect data['Adj Close'] to have shape (N days, 21 columns)
print("\nDownload complete. Columns in data:\n", data.columns)
prices_df = data["Adj Close"].copy()  # daily adjusted close
volume_df = data["Volume"].copy()     # daily volume

# Check a quick peek
print("\nSample of Adj Close data:")
print(prices_df.head())

#############################################
# 3. FEATURE ENGINEERING
#############################################

# A) Daily returns (percentage change)
returns_df = prices_df.pct_change()  # same shape as prices_df

# B) Example P/E ratio. We'll assign a single ratio per stock
#    (You could fetch real fundamentals per date if available).
pe_dict = {
    "AMZN": 150.0, "GOOG": 25.0,  "TSLA": 0.0,   "CRM": 100.0, "ADBE": 45.0,
    "BIIB": 20.0,  "ISRG": 35.0,  "VRTX": 28.0,  "REGN": 25.0, "ILMN": 50.0,
    "EBAY": 18.0,  "BIDU": 30.0,  "NFLX": 120.0, "BKNG": 30.0, "LULU": 40.0,
    "ADSK": 40.0,  "MU": 0.0,     "BMRN": 0.0,   "ALGN": 30.0, "UBER": 0.0,
    "EA": 20.0
}

# We'll transform data into a long format with columns: Date, Ticker, AdjClose, Volume, Return, ...
stacked_returns = returns_df.stack().reset_index()
stacked_returns.columns = ["Date", "Ticker", "Return"]
stacked_volume = volume_df.stack().reset_index()
stacked_volume.columns = ["Date", "Ticker", "Volume"]

# Merge returns and volume into single DataFrame
merged_df = pd.merge(stacked_returns, stacked_volume,
                     on=["Date", "Ticker"], how="inner")
merged_df.sort_values(["Ticker", "Date"], inplace=True)

# For each Ticker, compute rolling means of Return, rolling std of Return, and rolling means of Volume


def add_rolling_features(df):
    """
    df has columns: Date, Ticker, Return, Volume
    We'll add columns: MA_Return_5/20/90, Volatility_5/20/90, MA_Volume_5/20/90
    """
    # group by Ticker so rolling windows are per stock
    df = df.sort_values("Date").copy()
    for w in [5, 20, 90]:
        df[f"MA_Return_{w}"] = df["Return"].rolling(window=w).mean()
        df[f"Volatility_{w}"] = df["Return"].rolling(window=w).std()
        df[f"MA_Volume_{w}"] = df["Volume"].rolling(window=w).mean()
    return df


df_list = []
for ticker, grp in merged_df.groupby("Ticker"):
    grp_feat = add_rolling_features(grp)
    # add a P/E ratio column
    grp_feat["PE_ratio"] = pe_dict.get(ticker, 0.0)
    df_list.append(grp_feat)

features_df = pd.concat(df_list, ignore_index=True)
features_df.dropna(subset=["MA_Return_5", "Volatility_5",
                   "MA_Volume_5"], inplace=True)  # drop early rows per ticker

#############################################
# 4. DEFINE FORWARD RETURN & LABELS
#############################################

# We'll define Fwd_Return = Return(t+1) for next day
# so for each row, we shift Return by -1 within each ticker
features_df["Fwd_Return"] = features_df.groupby("Ticker")["Return"].shift(-1)
# drop last day of each ticker (no forward return)
features_df.dropna(subset=["Fwd_Return"], inplace=True)

# We'll define classes: +1 if Fwd_Return > tau, -1 if Fwd_Return < -tau, else 0
# Next we split train/test, then find tau from train so that ~1/3 are neutral there.

#############################################
# 5. TRAIN-TEST SPLIT (2009-2014 vs. 2015)
#############################################
train_end_date = datetime(2014, 12, 31)
mask_train = (features_df["Date"] <= train_end_date)
mask_test = (features_df["Date"] > train_end_date) & (
    features_df["Date"] <= datetime(2015, 11, 30))

train_data = features_df[mask_train].copy()
test_data = features_df[mask_test].copy()

# pick tau so ~1/3 training is neutral =>
# we want 1/3 of train_data with |Fwd_Return| <= tau
abs_returns = train_data["Fwd_Return"].abs().dropna()
tau = np.quantile(abs_returns, 0.33)
print(f"Chosen tau so that ~1/3 is neutral in train: {tau:.6f}")


def label_fwd(r, t):
    if r > t:
        return 1
    elif r < -t:
        return -1
    else:
        return 0


train_data["Label"] = train_data["Fwd_Return"].apply(
    lambda x: label_fwd(x, tau))
test_data["Label"] = test_data["Fwd_Return"].apply(lambda x: label_fwd(x, tau))

print("\nTrain label distribution:")
print(train_data["Label"].value_counts(normalize=True))

#############################################
# 6. PREPARE FEATURES FOR MODEL
#############################################
feature_cols = [
    "Return", "MA_Return_5", "MA_Return_20", "MA_Return_90",
    "Volatility_5", "Volatility_20", "Volatility_90",
    "Volume", "MA_Volume_5", "MA_Volume_20", "MA_Volume_90",
    "PE_ratio"
]

X_train = train_data[feature_cols].copy()
y_train = train_data["Label"]
X_test = test_data[feature_cols].copy()
y_test = test_data["Label"]

# drop any NaN rows
X_train.dropna(inplace=True)
y_train = y_train.loc[X_train.index]

X_test.dropna(inplace=True)
y_test = y_test.loc[X_test.index]

print("\nTraining samples:", len(X_train), "Testing samples:", len(X_test))

#############################################
# 7. TRAIN & EVALUATE 3 CLASSIFIERS
#############################################
# We'll do: LogisticRegression, RandomForest, XGBoost


# A) Logistic Regression
logreg = LogisticRegression(
    multi_class='multinomial', solver='lbfgs', max_iter=1000)
logreg.fit(X_train, y_train)
log_pred = logreg.predict(X_test)

print("\n=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, log_pred))
print("Confusion Matrix:\n", confusion_matrix(
    y_test, log_pred, labels=[-1, 0, 1]))
print("Classification Report:\n",
      classification_report(y_test, log_pred, labels=[-1, 0, 1], target_names=["-1", "0", "+1"]))

# B) Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("\n=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print("Confusion Matrix:\n", confusion_matrix(
    y_test, rf_pred, labels=[-1, 0, 1]))
print("Classification Report:\n",
      classification_report(y_test, rf_pred, labels=[-1, 0, 1], target_names=["-1", "0", "+1"]))

# C) XGBoost
xgb = XGBClassifier(use_label_encoder=False,
                    eval_metric='mlogloss', random_state=42)
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)

print("\n=== XGBoost ===")
print("Accuracy:", accuracy_score(y_test, xgb_pred))
print("Confusion Matrix:\n", confusion_matrix(
    y_test, xgb_pred, labels=[-1, 0, 1]))
print("Classification Report:\n",
      classification_report(y_test, xgb_pred, labels=[-1, 0, 1], target_names=["-1", "0", "+1"]))

print("\nDone! Check accuracy and classification reports above.")
