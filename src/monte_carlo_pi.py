"""
This module estimates π using the Monte Carlo method.

It generates random points uniformly in the unit square [0,1]×[0,1] and uses the
proportion of points inside the quarter circle (x² + y² ≤ 1) to form a running estimate of π.
The convergence of the running estimate is saved as a figure.
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n=10000):
    """
    Estimates π via Monte Carlo sampling in the unit square.

    Parameters:
        n (int): Number of random points to generate.

    Returns:
        None. Saves a convergence plot under ../results/figures/pi_estimation.png
    """
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    
    
    # x^2 + y^2 <= 1 koşulu (çeyrek daire içi)
    inside_circle = (x**2 + y**2) <= 1
    
    # Pi tahmini: 4 * (içeridekiler / toplam)
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
    
