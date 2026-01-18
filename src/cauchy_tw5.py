"""
TW5 – Distribution Comparison
Distribution: Cauchy(0, 1)

This script demonstrates the failure of both:
1) SLLN
2) CLT

Key theoretical facts:
- Mean does NOT exist
- Variance does NOT exist
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


x0 = 0
gamma = 1


n = 10000
samples = np.random.standard_cauchy(size=n)

cumulative_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.figure()
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.xlabel("n")
plt.ylabel("Sample Mean")
plt.title("SLLN – Cauchy(0,1)")
plt.legend()
plt.savefig("../results/cauchy/slln.png")
plt.close()


n_values = [2, 5, 10, 30, 50, 100]
m = 1000

for n in n_values:
    means = []

    for _ in range(m):
        sample = np.random.standard_cauchy(size=n)
        means.append(np.mean(sample))

    means = np.array(means)

    
    Z = means

    # Histogram
    plt.figure()
    plt.hist(Z, bins=50, density=True)
    plt.title(f"CLT Histogram – Cauchy, n={n}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.savefig(f"../results/cauchy/clt_hist_n{n}.png")
    plt.close()

    # QQ Plot
    plt.figure()
    stats.probplot(Z, plot=plt)
    plt.title(f"CLT QQ Plot – Cauchy, n={n}")
    plt.savefig(f"../results/cauchy/clt_qq_n{n}.png")
    plt.close()

