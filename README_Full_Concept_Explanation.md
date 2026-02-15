# Stochastic Derivatives Quant Lab

## Full Conceptual & Graph Interpretation Guide

------------------------------------------------------------------------

# 1. Project Purpose

This project builds a full derivatives research framework around SPY
options.\
It combines analytical pricing, stochastic simulation, volatility
surface extraction, nonlinear calibration, and second-order curvature
analysis.

The objective is not just to price options --- but to understand:

-   How parameters impact pricing
-   How sensitivities behave
-   How calibration geometry looks
-   How optimization stability can be diagnosed

------------------------------------------------------------------------

# 2. Black--Scholes Model

## What It Measures

The Black--Scholes model computes the theoretical fair value of a
European call option under assumptions of lognormal stock returns and
constant volatility.

Formula:

C = S N(d1) − K e\^(−rT) N(d2)

Where: - S = Spot price - K = Strike price - T = Time to maturity - r =
Risk-free rate - σ = Volatility

## Interpretation

If option price is high: - Volatility may be high - Time to maturity may
be long - Option may be deep in-the-money

High price is not inherently good or bad. It depends on whether you are
buying or selling.

------------------------------------------------------------------------

# 3. Monte Carlo Simulation

## What It Does

Simulates future stock paths using:

S_T = S_0 exp((r − σ²/2)T + σ√T Z)

The option price is the discounted expected payoff.

## Interpretation

If Monte Carlo ≈ Black--Scholes: - Model is correctly implemented -
Simulation converges

If Monte Carlo fluctuates heavily: - Too few simulations - High variance
estimator

Lower variance is better in simulation.

------------------------------------------------------------------------

# 4. Implied Volatility Surface

## What It Represents

Implied volatility is the volatility that makes model price equal to
market price.

Surface axes: - X: Strike - Y: Time to maturity - Z: Implied volatility

## Interpretation

High implied volatility means: - Market expects higher uncertainty -
Risk premium is expensive

Volatility skew reveals asymmetry in risk perception.

High IV is not "good" or "bad" --- it reflects market expectations.

------------------------------------------------------------------------

# 5. Greeks (Sensitivity Measures)

Greeks measure how option price reacts to small input changes.

## Delta

Sensitivity to spot price. High Delta → strong directional exposure.

## Gamma

Curvature with respect to spot. High Gamma → nonlinear explosive
sensitivity near ATM.

## Vega

Sensitivity to volatility. High Vega → price reacts strongly to
volatility changes.

High sensitivity increases risk exposure.

------------------------------------------------------------------------

# 6. Calibration Loss Surface

Loss function:

L(σ, r) = (Model Price − Market Price)\^2

## Interpretation

Low loss → good fit\
High loss → poor fit

Shape matters:

Convex bowl → stable optimization\
Flat surface → weak parameter identification\
Saddle shape → unstable region

Lower loss is better, but stable curvature is also important.

------------------------------------------------------------------------

# 7. Gradient Descent

Parameters updated via:

θ ← θ − α∇L

If descent path is smooth: - Landscape likely convex

If oscillating: - Learning rate too high

If stuck: - Flat region or saddle point

------------------------------------------------------------------------

# 8. Hessian & Curvature

Hessian contains second derivatives.

Eigenvalues interpretation:

Both positive → local minimum\
Mixed signs → saddle\
Both negative → local maximum

High curvature: - Very sensitive model - Steep loss surface

Low curvature: - Flat region - Parameters weakly identified

Moderate convex curvature is ideal.

------------------------------------------------------------------------

# 9. Graph Interpretations

Volatility Surface: Shows how market prices uncertainty.

Monte Carlo Plot: Shows stochastic convergence behavior.

Greeks Surface: Displays first and second-order risk sensitivities.

Loss Surface: Visualizes nonlinear calibration geometry.

Curvature Heatmap: Shows second-order optimization structure.

------------------------------------------------------------------------

# 10. Big Picture Flow

Market Data\
→ Extract Implied Volatility\
→ Fit Model\
→ Analyze Optimization Geometry\
→ Study Sensitivities\
→ Diagnose Curvature

This represents a full nonlinear derivatives research workflow.

------------------------------------------------------------------------

# 11. What "High" vs "Low" Means

  Metric         High Means              Low Means
  -------------- ----------------------- -----------------
  Option Price   Expensive premium       Cheap premium
  Volatility     High uncertainty        Calm market
  Delta          Strong directionality   Neutral
  Gamma          Strong convexity        Linear behavior
  Vega           Vol-sensitive           Vol-insensitive
  Loss           Poor fit                Good fit
  Curvature      Steep landscape         Flat region

There is no universal "good" or "bad" --- interpretation depends on
strategy, role, and risk exposure.

------------------------------------------------------------------------

# 12. Overall Insight

This project demonstrates:

-   Stochastic modeling
-   Surface reconstruction
-   Nonlinear optimization
-   Sensitivity analysis
-   Second-order curvature diagnostics

It bridges quantitative finance theory with interactive engineering
implementation.
