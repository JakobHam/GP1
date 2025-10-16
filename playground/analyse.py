import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv("Harmonic_oscilator.csv", skiprows=1,
                 names=['t', 'ax', 'ay', 'az'])


def model(t, delta, A, omega, phi): return np.exp(-delta *
                                                  t)*(2*A*np.cos(phi + omega*t))


popt, pcov = curve_fit(model, df['t'], df['ay'])

print(popt)
