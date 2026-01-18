"""
TW5 – Distribution Comparison
Distribution: Exponential(lambda = 1)

This script performs:
1) SLLN analysis (cumulative mean)
2) CLT analysis (histogram + QQ plots)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# --------------------------------------------------
# THEORETICAL MOMENTS
# --------------------------------------------------
mu = 1.0        # E[X] for Exponential(1)
sigma = 1.0     # Std dev for Exponential(1)

# --------------------------------------------------
# SLLN ANALYSIS
# --------------------------------------------------
n = 10000
samples = np.random.exponential(scale=1, size=n)

cumulative_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.figure()
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(y=mu, color="r", linestyle="--", label="E[X] = 1")
plt.xlabel("n")
plt.ylabel("Sample Mean")
plt.title("SLLN – Exponential(λ = 1)")
plt.legend()
plt.savefig("../results/exponential/slln.png")
plt.close()

# --------------------------------------------------
# CLT ANALYSIS
# --------------------------------------------------
n_values = [2, 5, 10, 30, 50, 100]
m = 1000

for n in n_values:
    means = []

    for _ in range(m):
        sample = np.random.exponential(scale=1, size=n)
        means.append(np.mean(sample))

    means = np.array(means)

    # Standardization (CLT valid: finite mean and variance)
    Z = (means - mu) / (sigma / np.sqrt(n))

    # Histogram
    plt.figure()
    plt.hist(Z, bins=30, density=True)
    plt.title(f"CLT Histogram – Exponential(1), n={n}")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.savefig(f"../results/exponential/clt_hist_n{n}.png")
    plt.close()

    # QQ Plot
    plt.figure()
    stats.probplot(Z, plot=plt)
    plt.title(f"CLT QQ Plot – Exponential(1), n={n}")
    plt.savefig(f"../results/exponential/clt_qq_n{n}.png")
    plt.close()

# --------------------------------------------------
# OBSERVATION
# --------------------------------------------------
# For the Exponential(1) distribution, both SLLN and CLT hold.
# However, compared to Uniform(0,1), convergence is slower due
# to skewness and heavier right tail.
