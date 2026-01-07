# IE221-Teamwork-Group22 Project

**Repository Setup and Simulation Code**

## Project Title and Description
Experimental Verification of the Strong Law of Large Numbers (SLLN) This project uses Monte Carlo simulations to demonstrate the SLLN. By generating random samples from a uniform distribution, we visualize how the sample mean ($\bar{X}_n$) almost surely converges to the theoretical expected value ($\mu$) as the number of trials ($n$) approaches infinity.In addition to SLLN, the project also includes simulations for the Central Limit Theorem (CLT)
and Monte Carlo estimation of π. All simulation outputs are saved under the results/figures directory.


---

## Team Members
- Yaren Görgülü – Student ID: 2211021064
- Fatmanur Demirci – Student ID: 2211021041
- Beyzanur Çiftçi- Student ID: 2211021008
- Buse Yakutsoy - Student ID:2311021070


---
## Installation
To run the simulations, Python 3 and the required libraries must be installed.

Install dependencies using:
```bash

pip install -r requirements.txt

python src/slln_simulation.py
python src/clt_simulation.py
python src/monte_carlo_pi.py



Project Structure

IE221-Teamwork-Group22/
│
├── src/
│   ├── slln_simulation.py        # SLLN simulation script
│   ├── clt_simulation.py         # CLT simulation script
│   └── monte_carlo_pi.py         # Monte Carlo π estimation
│
├── results/
│   └── figures/
│       ├── slln_running_mean.png # SLLN running mean convergence plot
│       ├── clt_histograms.png    # CLT histograms
│       ├── clt_qqplot.png        # CLT Q-Q plot
│       └── pi_estimation.png     # Monte Carlo π estimation
│
├── reports/
│   └── IE221_Teamwork_Group22_Report.pdf  # Final report
│
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── .gitignore                    # Files to ignore in GitHub

