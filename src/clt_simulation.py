"""
This module demonstrates the Central Limit Theorem (CLT) using i.i.d. Uniform(0,1) random variables.

For several sample sizes n, it generates m independent experiments, computes the standardized sum
Z = (S_n - n*mu) / (sigma*sqrt(n)), and compares the empirical distribution to N(0,1) using
histograms and a Q-Q plot.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def simulate_clt(n_values=[2, 5, 10, 30, 50], m=1000, bins=30):
    """
    Simulates the CLT for Uniform(0,1) variables.

    Parameters:
        n_values (list[int]): List of sample sizes n to test.
        m (int): Number of independent experiments for each n.
        bins (int): Number of histogram bins.

    Returns:
        dict[int, np.ndarray]: A dictionary mapping each n to its standardized sums (Z values).
    """
    mu, sigma = 0.5, np.sqrt(1 / 12)  # Mean and std for U[0,1]
    z_dict = {}

    fig, axes = plt.subplots(len(n_values), 1, figsize=(8, 4 * len(n_values)), sharex=True)

    # If only one subplot, make axes iterable
    if len(n_values) == 1:
        axes = [axes]

    for i, n in enumerate(n_values):
        # m experiments, each is the sum of n i.i.d U[0,1] variables
        sums = np.sum(np.random.uniform(0, 1, (m, n)), axis=1)

        # Standardization: Z = (S_n - n*mu) / (sigma*sqrt(n))
        z = (sums - n * mu) / (sigma * np.sqrt(n))
        z_dict[n] = z

        # Histogram of Z
        axes[i].hist(z, bins=bins, density=True, alpha=0.7)
        x = np.linspace(-4, 4, 200)
        axes[i].plot(x, stats.norm.pdf(x, 0, 1), lw=2)
        axes[i].set_title(f"Standardized sums (Z) for n = {n}")
        axes[i].set_ylabel("Density")
        axes[i].grid(True)

    axes[-1].set_xlabel("Z")
    plt.tight_layout()
    plt.savefig("../results/figures/clt_histograms.png", dpi=200)
    plt.show()

    return z_dict


def plot_qq(z_values, n_label):
    """
    Creates and saves a normal Q-Q plot for given standardized sums.

    Parameters:
        z_values (np.ndarray): Standardized sums (Z values).
        n_label (int): Sample size n for labeling the plot.

    Returns:
        None.
    """
    plt.figure(figsize=(8, 6))
    stats.probplot(z_values, dist="norm", plot=plt)
    plt.title(f"Normal Q-Q Plot for CLT (n = {n_label})")
    plt.xlabel("Theoretical Quantiles")
    plt.ylabel("Ordered Values")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../results/figures/clt_qqplot.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    z_dict = simulate_clt()
    # Use the largest n for the Q-Q plot (best normal approximation)
    n_max = max(z_dict.keys())
    plot_qq(z_dict[n_max], n_max)




