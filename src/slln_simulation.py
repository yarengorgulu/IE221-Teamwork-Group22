"""
This module demonstrates the Strong Law of Large Numbers (SLLN).

We generate i.i.d. samples from Uniform(0,1) and compute the running (cumulative) mean.
By the SLLN, the running mean converges almost surely to the true mean mu = 0.5.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_slln(n=10000):
    """
    Simulates the SLLN using i.i.d. Uniform(0,1) samples.

    Parameters:
        n (int): Number of samples.

    Returns:
        np.ndarray: Running mean values of length n.
    """
    mu = 0.5  # True mean of U(0,1)

    samples = np.random.uniform(0, 1, n)
    running_mean = np.cumsum(samples) / np.arange(1, n + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(running_mean, label="Running mean of U(0,1)")
    plt.axhline(y=mu, linestyle="--", label="True mean (0.5)")
    plt.xlabel("Number of samples (n)")
    plt.ylabel("Running mean")
    plt.title("SLLN Demonstration: Running Mean Converges to 0.5")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../results/figures/slln_running_mean.png", dpi=200)
    plt.show()

    return running_mean


if __name__ == "__main__":
    simulate_slln()


