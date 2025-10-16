import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

daten = [5.43, 5.269, 5.151, 4.361, 4.504]

mean = np.mean(daten)
std = np.std(daten)

#print(mean)
#print(std)



#####




x = [1., 1.5, 2., 2.5, 3.]
y= [3.049, 3.419, 4.058, 4.622, 4.892]
sigma_y = 0.1

f = lambda x,a,b: a+ b*x

popt, copt = curve_fit(f,x,y, sigma = sigma_y, absolute_sigma=True)

x_values = np.linspace(1,3,1000)
y_values = f(x_values, popt[0], popt[1])

plt.plot(x_values,y_values,color = 'blue', label = "model"  )
#plt.plot(x,y, linestyle = '.',color = 'black')
plt.errorbar(x,y, sigma_y,  fmt='.', capsize=5)
plt.xlabel("time (s)")
plt.ylabel('Voltage (V)')
plt.show()