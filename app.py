import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils import *

st.set_page_config(layout="wide")
st.title("🧠 Quant Research Lab — SPY Derivatives Terminal")

# ---------------------------------
# Cached Data Load
# ---------------------------------
@st.cache_data
def get_data():
    return load_spy_options()

S0, options_df = get_data()

# Sidebar Controls
st.sidebar.header("Global Controls")
r = st.sidebar.slider("Risk-Free Rate", 0.0, 0.1, 0.04)
learning_rate = st.sidebar.slider("Gradient Learning Rate", 0.001, 0.1, 0.01)
n_steps = st.sidebar.slider("Gradient Steps", 10, 80, 40)

tabs = st.tabs([
    "📈 Market",
    "🎲 Monte Carlo",
    "📊 Greeks",
    "🧮 Calibration",
    "🔍 Curvature"
])

# =========================================
# TAB 1 — MARKET
# =========================================
with tabs[0]:
    st.metric("SPY Spot Price", f"{S0:.2f}")
    st.dataframe(options_df.head())

# =========================================
# TAB 2 — MONTE CARLO
# =========================================
with tabs[1]:

    K = st.slider("Strike", float(S0*0.8), float(S0*1.2), float(S0))
    T = st.slider("Maturity (Years)", 0.1, 2.0, 1.0)
    sigma = st.slider("Volatility", 0.05, 0.6, 0.2)
    n_sim = st.slider("Simulations", 1000, 30000, 10000)

    bs_price = black_scholes_call(S0, K, T, r, sigma)
    mc_price = monte_carlo_call(S0, K, T, r, sigma, n_sim)

    col1, col2 = st.columns(2)
    col1.metric("Black–Scholes", f"{bs_price:.4f}")
    col2.metric("Monte Carlo", f"{mc_price:.4f}")

# =========================================
# TAB 3 — GREEKS
# =========================================
with tabs[2]:

    greek_type = st.selectbox("Select Greek", ["Delta", "Gamma", "Vega"])

    S_vals = np.linspace(S0*0.8, S0*1.2, 40)
    sigma_vals = np.linspace(0.05, 0.6, 40)

    S_grid, Sigma_grid = np.meshgrid(S_vals, sigma_vals)
    Z = np.zeros_like(S_grid)

    for i in range(len(sigma_vals)):
        for j in range(len(S_vals)):

            if greek_type == "Delta":
                Z[i,j] = delta_call(S_vals[j], S0, 1.0, r, sigma_vals[i])
            elif greek_type == "Gamma":
                Z[i,j] = gamma_call(S_vals[j], S0, 1.0, r, sigma_vals[i])
            else:
                Z[i,j] = vega_call(S_vals[j], S0, 1.0, r, sigma_vals[i])

    fig = go.Figure(data=[go.Surface(
        x=S_grid,
        y=Sigma_grid,
        z=Z,
        colorscale="Turbo"
    )])

    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# =========================================
# TAB 4 — CALIBRATION
# =========================================
with tabs[3]:

    K_atm = S0
    T_atm = 1.0
    market_price = black_scholes_call(S0, K_atm, T_atm, r, 0.25)

    sigma_vals = np.linspace(0.05, 0.6, 30)
    r_vals = np.linspace(0.01, 0.08, 30)

    Sigma, R = np.meshgrid(sigma_vals, r_vals)
    Loss = np.zeros_like(Sigma)

    for i in range(len(r_vals)):
        for j in range(len(sigma_vals)):
            model_price = black_scholes_call(
                S0, K_atm, T_atm, r_vals[i], sigma_vals[j]
            )
            Loss[i,j] = (model_price - market_price)**2

    fig = go.Figure(data=[go.Surface(
        x=Sigma,
        y=R,
        z=Loss,
        colorscale="Viridis"
    )])

    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# =========================================
# TAB 5 — CURVATURE
# =========================================
with tabs[4]:

    h = 1e-4
    Curvature = np.zeros_like(Sigma)

    for i in range(len(r_vals)):
        for j in range(len(sigma_vals)):

            sigma = sigma_vals[j]
            r_val = r_vals[i]

            Lss = (
                black_scholes_call(S0,K_atm,T_atm,r_val,sigma+h)
                - 2*black_scholes_call(S0,K_atm,T_atm,r_val,sigma)
                + black_scholes_call(S0,K_atm,T_atm,r_val,sigma-h)
            ) / h**2

            Lrr = (
                black_scholes_call(S0,K_atm,T_atm,r_val+h,sigma)
                - 2*black_scholes_call(S0,K_atm,T_atm,r_val,sigma)
                + black_scholes_call(S0,K_atm,T_atm,r_val-h,sigma)
            ) / h**2

            Curvature[i,j] = Lss + Lrr

    fig2 = go.Figure(data=go.Heatmap(
        x=sigma_vals,
        y=r_vals,
        z=Curvature,
        colorscale="Turbo"
    ))

    fig2.update_layout(template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)
