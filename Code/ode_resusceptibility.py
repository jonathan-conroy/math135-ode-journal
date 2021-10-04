import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint

N = 10000
MAXTIME = 1000

def plot(SIR_list):
    fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3)

    ax1.set_title("Susceptible")
    ax2.set_title("Infected")
    ax3.set_title("Removed")
    for (times, S, I, R, label) in SIR_list:
        ax1.plot(times, S, label = label)
        ax2.plot(times, I)
        ax3.plot(times, R)

    ax1.legend()
    plt.tight_layout()
    plt.show()

def simulate_sir_midpoint(alpha = 0.00013, beta = 1, resusceptibility = 0.01, maxtime = MAXTIME, delta_t = 1, n = 10000):
    # Alpha and n are chosen so that alpha * S[0] is slightly larger than 1
    # Maxtime is chosen by inspection
    times = np.arange(0, maxtime, step = delta_t)
    S = np.zeros(len(times))
    I = np.zeros(len(times))
    R = np.zeros(len(times))

    S[0] = n - 1
    I[0] = 1
    R[0] = 0

    for t in range(0, len(times) - 1):
        S_mid = S[t] - (alpha * I[t] * S[t] - resusceptibility * R[t]) * (delta_t/2)
        I_mid = I[t] -  beta * I[t] * (delta_t/2) + alpha * I[t] * S[t] * (delta_t/2)
        R_mid = R[t] + (beta * I[t] - resusceptibility * R[t])* (delta_t/2)

        S[t + 1] = S[t] - (alpha * I_mid * S_mid - resusceptibility * R_mid) * delta_t
        I[t + 1] = I[t] -  beta * I_mid * delta_t + alpha * I_mid * S_mid * delta_t
        R[t + 1] = R[t] + (beta * I_mid - resusceptibility * R_mid) * delta_t

    label = "Resusceptibility = {}".format(resusceptibility)
    return (times, S, I, R, label)

# Euler vs midpoint method: alpha = 0.00013, beta = 1
sir = simulate_sir_midpoint(alpha = 0.00013, delta_t = 0.5, resusceptibility = 0.01)
plot([sir, ])