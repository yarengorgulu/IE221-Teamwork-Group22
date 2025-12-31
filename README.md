# IE221-Teamwork-Group22 Project

**Repository Setup and Simulation Code**

## Project Title and Description
Experimental Verification of the Strong Law of Large Numbers (SLLN) This project uses Monte Carlo simulations to demonstrate the SLLN. By generating random samples from a uniform distribution, we visualize how the sample mean ($\bar{X}_n$) almost surely converges to the theoretical expected value ($\mu$) as the number of trials ($n$) approaches infinity.

---

## Team Members
- Yaren Görgülü – Student ID: 2211021064  
- Fatmanur Demirci – Student ID: 2211021041 
<!-- Add other team members here -->

---
## Installation
To run the simulations, Python 3 and the required libraries must be installed.

Install dependencies using:
```bash

pip install -r requirements.txt
python src/slln_simulation.py
results/figures/slln_convergence.png

-Project Structure
IE221-Teamwork-Group22/
│
├── src/
│   └── slln_simulation.py        # SLLN simulation script
│
├── results/
│   └── figures/
│       └── slln_convergence.png  # Generated SLLN convergence plot
│
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── .gitignore                    # Files to ignore in GitHub
