[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.17672840.svg)](https://doi.org/10.5281/zenodo.17672840)

# ΔN–ΔD Model: Reproducible Simulation Code

This repository contains the complete reproducible implementation of the **ΔN–ΔD Duality–Non-Equilibrium Model**, including all five simulations described in the manuscript.

The simulations numerically evaluate the structural dynamics:

\[
\frac{dS}{dt} = \alpha(\Delta N, \Delta D)\,\Delta N + \beta\,\Delta D,
\]

with the response function strictly following the formulation:

\[
\alpha(\Delta N, \Delta D) = 
\frac{A}{\left(1 + e^{-k(\Delta N - \Delta N_{\mathrm{crit}})}\right)\left(\Delta D^p + \varepsilon\right)}.
\]

All experiments use the canonical parameters:

- **A = 10.0**  
- **k = 8.0**  
- **ΔN₍crit₎ = 0.5**  
- **p = 2.0**  
- **ε = 0.01**  
- **β = 0.8**

---

## Included Simulations

### **1. Two-dimensional field of dS/dt over the (ΔN, ΔD) plane**
Numerical evaluation of the velocity field across the parameter space.

### **2. Threshold slices**
Cross-sections dS/dt(ΔN) for fixed ΔD values to illustrate the nonlinear threshold behaviour.

### **3. Endogenous dynamics over ΔD**
dS/dt as a function of ΔD for a small ΔN, demonstrating internal structural contribution.

### **4. Drift scenario ΔN(t)**
Simulation of a time-varying external gradient  
\[
\Delta N(t) = 0.5 + 0.3\sin(t),
\]
showing robust non-equilibrium dynamics and persistence of structure.

### **5. Minimization-based model (RL/FEP analog)**
A simple gradient-descent minimization model is simulated for comparison.  
Its dynamics converge to a fixed point (stasis), in contrast to the ΔN–ΔD model.

---

## Files

- **dn_dd_simulations.py** — full simulation code  
- **dn_dd_notebook.ipynb** — notebook version (Colab-friendly)  
- **requirements.txt** — dependencies  
- **/figures/** — placeholders for output images  

---

## Author

**Zhengis Tileubay**  
Kazakhstan, 2025

---

A Zenodo DOI will be added after the initial release.

