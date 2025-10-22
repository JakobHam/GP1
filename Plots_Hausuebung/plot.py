import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

#Data
position = np.array([10, 14, 23, 40, 46, 58, 63, 73, 98, 110])
potential = np.array([0.53, 0.67, 0.94, 1.27, 0.95, 1.49, 2.06, 2.30, 2.85, 3.06])
delta = np.array([0.05, 0.05, 0.05, 0.15, 0.05, 0.15, 0.15, 0.15, 0.15, 0.15]) 

#linear Model
model = lambda x, a, b: a*x+b

#Fitting
popt_weighted, covm_weighted = curve_fit(model, position, potential, sigma = delta, absolute_sigma=True)
popt, covm = curve_fit(model, position, potential)

# Chi**2
y_fit_weighted = model(position, *popt_weighted)
y_fit_unweighted = model(position, *popt)

N = len(position)
p = len(popt_weighted)

chi2_weighted = np.sum(((potential - y_fit_weighted) / delta) ** 2)
chi2_red_weighted = chi2_weighted / (N - p)

chi2_unweighted = np.sum(((potential - y_fit_unweighted) / delta) ** 2)
chi2_red_unweighted = chi2_unweighted / (N - p)

print(f"Weighted fit: reduced chi^2 = {chi2_red_weighted:.2f}")
print(f"Unweighted fit: reduced chi^2 = {chi2_red_unweighted:.2f}")

#Model calculation
nodes = np.linspace(0, 120, 10000) 
y_model_weighted = model(nodes, popt_weighted[0], popt_weighted[1])
y_model = model(nodes, popt[0], popt[1])

#plot
plt.plot(nodes, y_model_weighted, color = 'red', label='weigthed linear fit')
plt.plot(nodes, y_model, color = 'orange', label='unweigthed linear fit')
plt.errorbar(position, potential,delta,fmt = 'o',ls='none', color = 'blue', capsize=3, label= r"measurements with 1-$\sigma$ errorbars")
plt.xlabel("Distance (cm)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "LinFit_Plot.png"), dpi=600)
plt.show()