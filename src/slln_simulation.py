import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n=10000):
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
