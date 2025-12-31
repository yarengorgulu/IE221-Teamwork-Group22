import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_clt(n_values=[2, 5, 10, 30, 50], m=1000):
    mu, sigma = 0.5, np.sqrt(1/12) # U[0,1] için parametreler
    
    fig, axes = plt.subplots(len(n_values), 1, figsize=(8, 20))
    
    for i, n in enumerate(n_values):
        # m adet n'li toplam deneyi
        sums = np.sum(np.random.uniform(0, 1, (m, n)), axis=1)
        
        # Standartlaştırma: Zi = (Sn - n*mu) / (sigma * sqrt(n))
        standardized_sums = (sums - n * mu) / (sigma * np.sqrt(n))
        
        # Histogram
        axes[i].hist(standardized_sums, bins=30, density=True, alpha=0.6, color='skyblue')
        
        # Standart Normal Eğrisi (N(0,1))
        x = np.linspace(-4, 4, 100)
        axes[i].plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2)
        axes[i].set_title(f'n = {n} için Standartlaştırılmış Toplamlar')
        
    plt.tight_layout()
    plt.savefig('../results/figures/clt_histograms.png')
    plt.show()

if __name__ == "__main__":
    simulate_clt()



^#qqplots
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

data = np.random.normal(0, 1, 1000) 

plt.figure(figsize=(8, 6))
stats.probplot(data, dist="norm", plot=plt)

plt.title('Normal Q-Q Plot (n=50)')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)


plt.savefig('results/figures/clt_qqplots.png')
plt.show()
