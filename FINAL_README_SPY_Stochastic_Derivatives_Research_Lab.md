# SPY Stochastic Derivatives Research Lab

## Advanced Option Pricing, Volatility Surface Reconstruction & Nonlinear Calibration Framework

------------------------------------------------------------------------

## 🌐 Live Demo

Interactive Streamlit App:\
👉
https://spy-volatility-surface-calibration-mpi3rwpv4watjzlwfaphlw.streamlit.app/

------------------------------------------------------------------------

# 📌 Project Overview

The **SPY Stochastic Derivatives Research Lab** is a quantitative
finance research framework built around real SPY option market data.

It integrates:

-   Black--Scholes analytical pricing
-   Monte Carlo stochastic simulation
-   Implied volatility surface reconstruction
-   Nonlinear parameter calibration
-   Gradient-based optimization
-   Greeks sensitivity surfaces
-   Hessian curvature diagnostics
-   Interactive Streamlit visualization

This is a structured derivatives research engine --- not just a pricing
demo.

------------------------------------------------------------------------

# 🎯 Core Objective

The purpose of this project is to understand:

• How option prices respond to parameter changes\
• How market-implied volatility behaves across strikes and maturities\
• How calibration landscapes look geometrically\
• How optimization stability can be diagnosed using first- and
second-order derivatives

It bridges mathematical finance theory with deployable quantitative
engineering.

------------------------------------------------------------------------

# 📊 Data Sources

The project uses live and real-world financial data:

  Data Type          Source
  ------------------ ------------------------------------
  SPY Spot Price     Yahoo Finance API (via `yfinance`)
  SPY Option Chain   Yahoo Finance Options Data
  Risk-Free Rate     User-controlled input parameter

Data is fetched dynamically using:

import yfinance as yf

This allows real-time surface reconstruction and calibration
experiments.

------------------------------------------------------------------------

# 🧮 Model Components

## 1️⃣ Black--Scholes Pricing

European call price:

C = S₀ N(d₁) − K e\^(−rT) N(d₂)

Higher volatility → Higher option price\
Longer maturity → Higher time value

------------------------------------------------------------------------

## 2️⃣ Monte Carlo Simulation

Stock evolution:

S_T = S₀ exp((r − σ²/2)T + σ√T Z)

Used to numerically approximate theoretical prices and validate
analytical results.

------------------------------------------------------------------------

## 3️⃣ Implied Volatility Surface

Extracted by solving:

C_market = C_model(σ)

3D Surface Axes:

-   Strike
-   Time to maturity
-   Implied volatility

Reveals volatility skew and term structure.

------------------------------------------------------------------------

## 4️⃣ Greeks Sensitivity Surfaces

  Greek   Meaning
  ------- ---------------------------
  Delta   Sensitivity to spot
  Gamma   Curvature w.r.t spot
  Vega    Sensitivity to volatility

These surfaces visualize first- and second-order risk exposures.

------------------------------------------------------------------------

## 5️⃣ Calibration Loss Surface

Loss function:

L(σ, r) = (C_model − C_market)²

Visualized as a 3D optimization landscape to study convexity and
parameter sensitivity.

------------------------------------------------------------------------

## 6️⃣ Gradient Descent Optimization

Parameters updated via:

θ ← θ − α∇L

Shows how model parameters converge toward optimal fit.

------------------------------------------------------------------------

## 7️⃣ Hessian & Curvature Diagnostics

Second-order derivatives computed numerically.

Eigenvalues determine:

-   Convex region
-   Saddle region
-   Local maximum

Curvature heatmaps visualize optimization stability.

------------------------------------------------------------------------

# 📈 High vs Low --- Interpretation Guide

  Metric               High Means                    Low Means
  -------------------- ----------------------------- ------------------
  Option Price         Expensive premium             Cheap premium
  Implied Volatility   High uncertainty              Calm market
  Delta                Strong directionality         Neutral exposure
  Gamma                Strong convexity              Linear payoff
  Vega                 High volatility sensitivity   Vol-insensitive
  Loss                 Poor fit                      Good fit
  Curvature            Steep geometry                Flat region

There is no universal "good" or "bad" --- interpretation depends on
strategy and risk exposure.

------------------------------------------------------------------------

# 🖥 Streamlit Application Structure

Tabs include:

-   📈 Market Data Overview
-   🎲 Monte Carlo Pricing Engine
-   📊 Greeks 3D Surfaces
-   🧮 Calibration Loss Landscape
-   🔍 Curvature & Hessian Diagnostics

The app provides interactive parameter controls for:

-   Volatility
-   Risk-free rate
-   Strike
-   Maturity
-   Simulation count
-   Gradient steps

------------------------------------------------------------------------

# 🏗 Technical Stack

-   Python 3.11
-   NumPy
-   SciPy
-   Pandas
-   yfinance
-   Plotly (3D Visualization)
-   Streamlit (Deployment)

------------------------------------------------------------------------

# 🚀 How To Run Locally

pip install streamlit plotly yfinance scipy pandas numpy\
streamlit run app.py

------------------------------------------------------------------------

# 🔮 Future Extensions

-   Multi-strike calibration
-   Stochastic volatility models (Heston)
-   Local volatility surface fitting
-   Variance reduction techniques
-   Risk-neutral density extraction

------------------------------------------------------------------------

# 📌 Summary

The **SPY Stochastic Derivatives Research Lab** reconstructs the SPY
volatility surface, simulates stochastic pricing via Monte Carlo,
performs nonlinear calibration, and analyzes second-order curvature
using Hessian diagnostics --- all inside an interactive research
terminal.

It demonstrates quantitative finance theory integrated with deployable
engineering infrastructure.
