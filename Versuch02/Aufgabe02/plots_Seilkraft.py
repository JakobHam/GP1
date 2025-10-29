import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import umath
import pandas as pd
import os




df9 = pd.read_csv("Aufgabe02/9Grad_Force.csv",skiprows=1, names = ["index", "frame", "sample", "time", 'raw Force', "Force"])
df15 = pd.read_csv("Aufgabe02/15Grad_Force.csv",skiprows=1, names = ["index", "frame", "sample", "time", 'raw Force', "Force"])
df30 = pd.read_csv("Aufgabe02/30Grad_Force.csv",skiprows=1, names = ["index", "frame", "sample", "time", 'raw Force', "Force"])

plt.plot(df15["time"], df15["Force"])
plt.xlim(15, 40)
plt.ylim(-2.25, -1.95)
plt.vlines(23.39, ymin = -5, ymax=0,color ="#f39200", label=r'$t_1 = 23{,}39(2) \, \mathrm{s}$')#003361
#plt.vlines(38.39, ymin = -5, ymax=0,color ="#f39200", label=r'$t_2 = 38{,}39(2) \, \mathrm{s}$')#003361
#plt.vlines(23.37, ymin = -5, ymax=0,color ="red", label = "Fehlergrenzen")#003361
#plt.vlines(23.41, ymin = -5, ymax=0,color ="red")#003361
plt.legend()
plt.xlabel("Zeit (s)")
plt.ylabel("Kraft (N)")
plt.tight_layout()
#plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Force30_Plot.png"), dpi=600)
plt.show()


