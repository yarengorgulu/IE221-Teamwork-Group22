"""
TW5 – Distribution Comparison
Distribution: Pareto(alpha = 3, x_m = 1)

This script performs:
1) SLLN analysis (cumulative mean)
2) CLT analysis (histogram + QQ plots)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


alpha = 3
x_m = 1

mu = (alpha * x_m) / (alpha - 1)          # E[X] = 3 / 2
sigma = np.sqrt((alpha * x_m**2) / ((alpha - 1)**2 * (alpha - 2)))  # sqrt(3/4)


n = 10000
samples = np.random.pareto(alpha, size=n) + x_m

cumulative_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.figure()
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(y=mu, color="r", linestyle="--", label="E[X] = 1.5")
plt.xlabel("n")
plt.ylabel("Sample Mean")
plt.title("SLLN – Pareto(α = 3)")
plt.legend()
plt.savefig("../results/pareto_alpha3/slln.png")
plt.close()

n_values = [2, 5, 10, 30, 50, 100]
m = 1000

for n in n_values:
    means = []

    for _ in range(m):
        sample = np.random.pareto(alpha, size=n) + x_m
        means.append(np.mean(sample))

    means = np.array(means)

 
    Z = (means - mu) / (sigma / np.sqrt(n))

    # Histogram
    plt.figure()
    plt.hist(Z, bins=30, density=True)
    plt.title(f"CLT Histogram – Pareto(α=3), n={n}")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.savefig(f"../results/pareto_alpha3/clt_hist_n{n}.png")
    plt.close()

    # QQ Plot
    plt.figure()
    stats.probplot(Z, plot=plt)
    plt.title(f"CLT QQ Plot – Pareto(α=3), n={n}")
    plt.savefig(f"../results/pareto_alpha3/clt_qq_n{n}.png")
    plt.close()


