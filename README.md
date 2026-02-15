
# 🧠 SPY Volatility Surface Calibration
## SPY Volatility Surface, Monte Carlo Pricing & Nonlinear Calibration Framework

---

# 📌 Project Overview

This project builds a full **derivatives research engine** around SPY options, combining:

- Black–Scholes analytical pricing
- Monte Carlo simulation
- Implied volatility surface extraction
- 3D calibration loss landscapes
- Gradient descent optimization
- Greeks surface visualization
- Hessian curvature analysis

The result is an interactive **Streamlit-based Quant Research Terminal** built on real market data.

This is not a toy pricing demo — it is a structured nonlinear optimization and sensitivity analysis lab.

---

# 🧭 Project Roadmap (Phases 1–7)

---

## 🔹 Phase 1 — Black–Scholes Pricing Engine

Implemented analytical European call pricing from scratch:

C = S N(d1) − K e^(−rT) N(d2)

Also implemented core Greeks:
- Delta
- Gamma
- Vega

Purpose:
- Establish analytical baseline
- Enable sensitivity and calibration analysis

---

## 🔹 Phase 2 — Monte Carlo Simulation Engine

Simulated risk-neutral stock paths:

S_T = S_0 exp((r − σ²/2)T + σ√T Z)

Computed discounted expected payoff:

C = e^(−rT) E[max(S_T − K, 0)]

Compared Monte Carlo price vs Black–Scholes to validate stochastic engine.

Added convergence visualization to demonstrate simulation stability.

Purpose:
- Validate stochastic modeling
- Demonstrate numerical approximation of analytical solution

---

## 🔹 Phase 3 — Live SPY Option Chain Integration

Pulled real market data using `yfinance`:

- SPY spot price
- Real expiration dates
- Real strike grid
- Real market prices

Converted expiration to time-to-maturity T.

Purpose:
- Move from synthetic modeling to real market structure
- Enable realistic surface construction

---

## 🔹 Phase 4 — Implied Volatility Extraction

Used Newton–Raphson root-finding to solve:

C_market = C_BS(σ)

Computed implied volatility per strike and maturity.

Built 3D volatility surface:

Strike × Maturity × Implied Vol

Purpose:
- Reconstruct market volatility structure
- Analyze volatility skew and term structure

---

## 🔹 Phase 5 — Calibration Loss Surface

Defined calibration objective:

L(σ, r) = (C_model − C_market)²

Constructed 3D loss surface across parameter grid:

σ × r × Loss

Purpose:
- Visualize optimization landscape
- Identify convex regions
- Understand parameter sensitivity

---

## 🔹 Phase 6 — Gradient Descent Optimization

Implemented numerical gradient via finite differences.

Ran iterative descent:

θ ← θ − α ∇L

Tracked trajectory across surface.

Visualized descent path in 3D.

Purpose:
- Demonstrate nonlinear calibration
- Show optimization geometry in action

---

## 🔹 Phase 7 — Hessian & Curvature Analysis

Computed second-order derivatives numerically:

∂²L/∂σ²  
∂²L/∂r²  
∂²L/∂σ∂r  

Constructed Hessian matrix and analyzed curvature via:

- Eigenvalues
- Trace(H)
- Convexity diagnostics

Built curvature heatmap across parameter space.

Purpose:
- Understand local convexity
- Identify saddle regions
- Demonstrate second-order optimization insight

---

# 🖥 Streamlit Quant Research Terminal

The final implementation integrates all components into a structured UI-https://spy-volatility-surface-calibration-mpi3rwpv4watjzlwfaphlw.streamlit.app/

## 📈 Market Tab
- Displays live SPY price
- Shows option snapshot

## 🎲 Monte Carlo Tab
- Adjustable strike, maturity, volatility
- Monte Carlo vs Black–Scholes comparison
- Demonstrates stochastic convergence

## 📊 Greeks Tab
Interactive 3D surfaces for:
- Delta
- Gamma
- Vega

Axes:
- Spot price
- Volatility

Purpose:
- Visualize first- and second-order sensitivities

## 🧮 Calibration Tab
- 3D loss surface
- Visualizes nonlinear objective landscape

## 🔍 Curvature Tab
- Hessian-based curvature heatmap
- Shows convexity structure across parameter grid
- Highlights optimization geometry

---

# 🏗 Technical Stack

- Python 3.11
- NumPy
- SciPy
- Plotly (3D visualization)
- yfinance (live data ingestion)
- Streamlit (interactive UI)

---

# 🎯 Key Concepts Demonstrated

- Stochastic calculus intuition
- Monte Carlo simulation
- Volatility surface reconstruction
- Nonlinear parameter calibration
- Gradient-based optimization
- Second-order curvature analysis
- Derivatives sensitivity modeling

---

# 🚀 How To Run

pip install streamlit plotly yfinance scipy pandas numpy  
streamlit run app.py

---

# 🧠 Positioning

This project bridges:

- Quantitative Finance (derivatives modeling)
- Numerical Optimization (gradient & Hessian analysis)
- Software Engineering (modular architecture)
- Data Engineering (live market ingestion)

It is structured as a reusable derivatives research framework, not a single-use notebook.


---

# 📌 Summary

Built a real-time derivatives research terminal that reconstructs the SPY volatility surface, simulates option pricing via Monte Carlo, calibrates model parameters using gradient descent, and analyzes second-order curvature via Hessian diagnostics.

This project demonstrates advanced quantitative finance modeling integrated with interactive engineering infrastructure.
