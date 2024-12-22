import pandas as pd
import numpy as np
from math import exp, log, sqrt, pi
from scipy.stats import norm

S_e_minus_qT = 2360.1743583417406
e_minus_rT = 0.993169427730553
S = 2381
T = 138/252

q = -log(S_e_minus_qT / S) / T
r = -log(e_minus_rT) / T

F = S_e_minus_qT * 1/e_minus_rT

df = pd.read_csv("prices.csv")

df["y"] = np.log(F/df["Strike"])
df["alpha_C"] = df["Mid_Call"]/(df["Strike"] * exp(-r*T))
df["R_C"] = 2*df["alpha_C"] - np.exp(df["y"]) + 1
df["B_C"] = 4 * (np.exp((2/pi)*df["y"]) + np.exp(-(2/pi)*df["y"])) - 2*np.exp(-df["y"])*(np.exp(
    (1-2/pi)*df["y"]) + np.exp(-(1-2/pi)*df["y"])) * (np.exp(2*df["y"]) + 1 - np.power(df["R_C"], 2))
df["C_C"] = np.exp(-2*df["y"]) * (np.power(df["R_C"], 2) - np.power(np.exp(
    df["y"]) - 1, 2)) * (np.power(np.exp(df["y"] + 1), 2) - np.power(df["R_C"], 2))

df["A"] = np.power(np.exp((1-2/pi)*df["y"]) - np.exp(-(1-2/pi)*df["y"]), 2)


def A(y: float) -> float:
    return (exp((1-2/pi)*y) - exp(-(1-2/pi)*y))**2


df["alpha_P"] = df["Mid_Put"]/(df["Strike"] * exp(-r*T))
df["R_P"] = 2*df["alpha_P"] + np.exp(df["y"]) - 1
df["B_P"] = 4*(np.exp((2/pi)*df["y"]) + np.exp(-(2/pi)*df["y"])) - 2*np.exp(-df["y"])*(np.exp((1-2/pi)
                                                                                              * df["y"]) + np.exp(-(1-2/pi)*df["y"])) * (np.exp(2*df["y"]) + 1 - np.power(df["R_P"], 2))
df["C_P"] = np.exp(-2*df["y"]) * (np.power(df["R_P"], 2) - np.power(np.exp(
    df["y"]) - 1, 2)) * (np.power(np.exp(df["y"] + 1), 2) - np.power(df["R_P"], 2))

df["beta_C"] = 2 * df["C_C"] / \
    (df["B_C"] + np.sqrt(np.power(df["B_C"], 2) + 4*df["A"]*df["C_C"]))
df["gamma_C"] = -pi/2*np.log(df["beta_C"])

df["beta_P"] = 2 * df["C_P"] / \
    (df["B_P"] + np.sqrt(np.power(df["B_P"], 2) + 4*df["A"]*df["C_P"]))
df["gamma_P"] = -pi/2*np.log(df["beta_P"])

df["CP_00"] = df["Strike"]*np.exp(-r*T)


def calculate_sigma_c(row):
    g = row["gamma_C"]
    y = row["y"]
    if y >= 0:
        C_0 = row["CP_00"] * (exp(y) * A(sqrt(2*y)) - 1/2)
        if row['Mid_Call'] <= C_0:
            return 1 / sqrt(T) * (sqrt(g+y) - sqrt(g-y))
        else:
            return 1 / sqrt(T) * (sqrt(g+y) + sqrt(g-y))
    else:
        C_0 = row["CP_00"] * (exp(y)/2 - A(-sqrt(-2*y)))
        if row['Mid_Call'] <= C_0:
            return 1 / sqrt(T) * (-sqrt(g+y) + sqrt(g-y))
        else:
            return 1 / sqrt(T) * (sqrt(g+y) + sqrt(g-y))


def calculate_sigma_p(row):
    g = row["gamma_P"]
    y = row["y"]
    if y >= 0:
        P_0 = row["CP_00"] * (1/2 - exp(y) * A(-sqrt(2*y)))
        if row['Mid_Call'] <= P_0:
            return 1 / sqrt(T) * (sqrt(g+y) - sqrt(g-y))
        else:
            return 1 / sqrt(T) * (sqrt(g+y) + sqrt(g-y))
    else:
        P_0 = row["CP_00"] * (A(sqrt(-2*y)) - exp(y)/2)
        if row['Mid_Call'] <= P_0:
            return 1 / sqrt(T) * (-sqrt(g+y) + sqrt(g-y))
        else:
            return 1 / sqrt(T) * (sqrt(g+y) + sqrt(g-y))

# Apply calculation to DataFrame
# df['sigma_C'] = df.apply(calculate_sigma_c, axis=1)
# df['sigma_P'] = df.apply(calculate_sigma_p, axis=1)


df
