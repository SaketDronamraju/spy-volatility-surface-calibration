import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm
from datetime import datetime

# -----------------------------
# Black–Scholes
# -----------------------------
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 5e-1*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def delta_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return norm.cdf(d1)

def gamma_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return norm.pdf(d1)/(S*sigma*np.sqrt(T))

def vega_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return S*norm.pdf(d1)*np.sqrt(T)

# -----------------------------
# Monte Carlo
# -----------------------------
def monte_carlo_call(S, K, T, r, sigma, n_sim=10000):
    Z = np.random.normal(0,1,n_sim)
    ST = S*np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST-K,0)
    return np.exp(-r*T)*np.mean(payoff)

# -----------------------------
# Load SPY Options
# -----------------------------
def load_spy_options():
    ticker = yf.Ticker("SPY")
    S0 = ticker.history(period="1d")["Close"].iloc[-1]
    expirations = ticker.options[:2]

    data = []
    today = datetime.today()

    for expiry in expirations:
        chain = ticker.option_chain(expiry)
        calls = chain.calls.copy()
        calls["expiration"] = expiry
        data.append(calls)

    df = pd.concat(data)
    df["T"] = df["expiration"].apply(
        lambda x: (datetime.strptime(x,"%Y-%m-%d") - today).days/365
    )

    df = df[df["T"] > 0]
    df = df.dropna(subset=["lastPrice"])

    return S0, df

