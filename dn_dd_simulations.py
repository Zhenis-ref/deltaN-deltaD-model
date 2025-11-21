import numpy as np
import matplotlib.pyplot as plt

# =====================================
# CANONICAL PARAMETERS OF THE MODEL
# =====================================

A = 10.0
k = 8.0
N_CRIT = 0.5
p = 2.0
EPS = 0.01
BETA = 0.8


# =====================================
# RESPONSE FUNCTION α(ΔN, ΔD)
# =====================================

def alpha_deltaN_deltaD(deltaN, deltaD,
                        A=A, k=k, N_crit=N_CRIT,
                        p=p, eps=EPS):

    logistic = 1.0 + np.exp(-k * (deltaN - N_crit))
    suppression = (deltaD ** p) + eps
    return A / (logistic * suppression)


# =====================================
# EQUATION dS/dt
# =====================================

def dSdt(deltaN, deltaD):
    return alpha_deltaN_deltaD(deltaN, deltaD) * deltaN + BETA * deltaD


# =====================================
# (1) 2D MAP OVER (ΔN, ΔD)
# =====================================

def simulate_heatmap(n=200):
    N = np.linspace(0, 1, n)
    D = np.linspace(0, 1, n)
    Z = np.zeros((n, n))

    for i, nval in enumerate(N):
        for j, dval in enumerate(D):
            Z[j, i] = dSdt(nval, dval)

    plt.figure(figsize=(7, 6))
    plt.imshow(Z, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
    plt.colorbar(label='dS/dt')
    plt.xlabel('ΔN')
    plt.ylabel('ΔD')
    plt.title('Two-dimensional field of dS/dt over (ΔN, ΔD)')
    plt.tight_layout()
    plt.show()


# =====================================
# (2) THRESHOLD SLICES
# =====================================

def simulate_threshold_slices():
    N = np.linspace(0, 1, 400)

    plt.figure(figsize=(7, 6))
    for D0 in [0.0, 0.2, 0.4, 0.6, 0.8]:
        curve = [dSdt(n, D0) for n in N]
        plt.plot(N, curve, label=f'D = {D0}')

    plt.xlabel('ΔN')
    plt.ylabel('dS/dt')
    plt.title('Threshold curves of dS/dt for different ΔD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# =====================================
# (3) ENDOGENOUS ΔD DYNAMICS
# =====================================

def simulate_endogenous_dynamics(N0=0.1, steps=200):
    D = np.linspace(0, 1, 400)
    curve = [dSdt(N0, d) for d in D]

    plt.figure(figsize=(7, 6))
    plt.plot(D, curve)
    plt.xlabel('ΔD')
    plt.ylabel('dS/dt')
    plt.title(f'Endogenous dS/dt as a function of ΔD (ΔN={N0})')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# =====================================
# (4) DRIFT SCENARIO
# =====================================

def simulate_drift_scenario(T=2000, dt=0.01):
    t = np.arange(0, T*dt, dt)
    N = 0.5 + 0.3 * np.sin(t)
    D = 0.5

    S = np.zeros_like(t)
    dS_series = np.zeros_like(t)

    for i in range(1, len(t)):
        ds = dSdt(N[i], D)
        dS_series[i] = ds
        S[i] = S[i-1] + ds * dt

    plt.figure(figsize=(8, 6))
    plt.plot(t, dS_series)
    plt.title('Drift Scenario: dS/dt over time')
    plt.xlabel('Time')
    plt.ylabel('dS/dt')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(t, S)
    plt.title('Integrated S(t) under drift ΔN(t)')
    plt.xlabel('Time')
    plt.ylabel('S(t)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# =====================================
# (5) MINIMIZATION MODEL COMPARISON
# =====================================

def simulate_minimization(T=2000, dt=0.01):
    x = 1.0
    eta = 0.01
    traj = []

    for _ in range(T):
        grad = x  
        x -= eta * grad
        traj.append(x)

    plt.figure(figsize=(8, 6))
    plt.plot(traj)
    plt.title('Minimization Dynamics (RL/FEP analog)')
    plt.xlabel('Iteration')
    plt.ylabel('State x')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
