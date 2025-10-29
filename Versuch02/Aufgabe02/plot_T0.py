import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import umath
import pandas as pd
import os

g =9.8051

t19 = ufloat(14.30,0.07)
t29 = ufloat(29.16,0.08)

t115 = ufloat(15.34,0.06)
t215 = ufloat(30.25, 0.06)

t130 = ufloat(23.39, 0.02)
t230 = ufloat(38.39, 0.02)

delta9 = t29 - t19
delta15 = t215 - t115
delta30 = t230 - t130

T_0=[delta9 / 10, delta15 / 10, delta30 /10]
T0_value = [x.n for x in T_0]
T0_std = [x.s for x in T_0]

theta = [9, 15, 30]

model_1 = 2 * const.pi * np.sqrt(0.544 / g)
model_2 = lambda theta: 2 * const.pi *(1 + np.deg2rad(theta)**2 /16)* np.sqrt(0.544 / g)

x_values = np.linspace(7, 32, 10000)
y_values1 = [model_1 for x in x_values]
y_values2 = model_2(x_values)


diff = T_0[2] - model_1

ver = diff.n/diff.s

print(ver)

plt.errorbar(theta, T0_value,T0_std, 2,  fmt = 'o',color = "#003361",ls='none', capsize=3, label = r"Messwerte für $T_0$")
plt.plot(x_values, y_values1,color = "red" , label = r"$T_0 =2\pi \sqrt{\frac{L}{g}}$")
plt.plot(x_values, y_values2, color = "#f39200",label = r"$T_0 = 2\pi (1+\frac{\theta^2_0}{16})\sqrt{\frac{L}{g}}$")
#plt.xlim(15, 40)
#plt.ylim(-2.25, -1.95)
#plt.vlines(23.39, ymin = -5, ymax=0,color ="#f39200", label=r'$t_1 = 23{,}39(2) \, \mathrm{s}$')#003361
#plt.vlines(38.39, ymin = -5, ymax=0,color ="#f39200", label=r'$t_2 = 38{,}39(2) \, \mathrm{s}$')#003361
#plt.vlines(23.37, ymin = -5, ymax=0,color ="red", label = "Fehlergrenzen")#003361
#plt.vlines(23.41, ymin = -5, ymax=0,color ="red")#003361
plt.legend()
plt.xlabel(r"Winkel $\theta_0$ (◦)")
plt.ylabel(r"Periodendauer $T_0$ (s)")
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Periodendauer.png"), dpi=600)

