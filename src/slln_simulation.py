"""
This module demonstrates the Strong Law of Large Numbers (SLLN)
using a Monte Carlo simulation to estimate the value of π.

As the number of random samples increases, the estimator converges
almost surely to the true value of π, illustrating the SLLN in practice.
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n=10000):
        """
    Estimates the value of π using the Monte Carlo method.

    Random points are generated uniformly in the unit square [0,1] × [0,1].
    The proportion of points that fall inside the quarter circle
    (x² + y² ≤ 1) is used to estimate π.

    Parameters:
        n (int): Number of random points generated.

    Returns:
        None. The function generates a convergence plot and saves it as an image.
    """
# Generate n random points uniformly in the unit square
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    
    # x^2 + y^2 <= 1 koşulu (çeyrek daire içi)
# Check whether points fall inside the quarter circle
    inside_circle = (x**2 + y**2) <= 1
    
    # Pi tahmini: 4 * (içeridekiler / toplam)
# Running Monte Carlo estimate of π using cumulative averages
    pi_estimates = 4 * np.cumsum(inside_circle) / np.arange(1, n + 1)
    
    # Görselleştirme
    plt.figure(figsize=(10, 6))
    plt.plot(pi_estimates, label='Pi Tahmini')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='Gerçek Pi Değeri')
    plt.xlabel('Nokta Sayısı (n)')
    plt.ylabel('Tahmin Edilen Değer')
    plt.title('Monte Carlo ile Pi Sayısı Tahmini')
    plt.legend()
    plt.grid(True)
    plt.savefig('../results/figures/pi_estimation.png')
    plt.show()

if __name__ == "__main__":
    estimate_pi()
