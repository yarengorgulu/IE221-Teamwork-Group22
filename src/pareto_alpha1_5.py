"""
TW5 – Distribution Comparison
Distribution: Pareto(alpha = 1.5, x_m = 1)

This script performs:
1) SLLN analysis (cumulative mean)
2) CLT analysis (demonstration of failure)

Key theoretical fact:
- Mean exists
- Variance is infinite
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


alpha = 1.5
x_m = 1

mu = (alpha * x_m) / (alpha - 1)   # E[X] = 3
# Variance does NOT exist for alpha <= 2
# sigma is undefined (infinite variance)


n = 10000
samples = np.random.pareto(alpha, size=n) + x_m

cumulative_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.figure()
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(y=mu, color="r", linestyle="--", label="E[X] = 3")
plt.xlabel("n")
plt.ylabel("Sample Mean")
plt.title("SLLN – Pareto(α = 1.5)")
plt.legend()
plt.savefig("../results/pareto_alpha1_5/slln.png")
plt.close()


n_values = [2, 5, 10, 30, 50, 100]
m = 1000

for n in n_values:
    means = []

    for _ in range(m):
        sample = np.random.pareto(alpha, size=n) + x_m
        means.append(np.mean(sample))

    means = np.array(means)

   
    Z = means   # intentionally not standardized

    # Histogram
    plt.figure()
    plt.hist(Z, bins=30, density=True)
    plt.title(f"CLT Histogram – Pareto(α=1.5), n={n}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.savefig(f"../results/pareto_alpha1_5/clt_hist_n{n}.png")
    plt.close()

    # QQ Plot
    plt.figure()
    stats.probplot(Z, plot=plt)
    plt.title(f"CLT QQ Plot – Pareto(α=1.5), n={n}")
    plt.savefig(f"../results/pareto_alpha1_5/clt_qq_n{n}.png")
    plt.close()


