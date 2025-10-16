import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy  as np

filename = "data01.csv"

df = pd.read_csv(filename,skiprows=1, names = ["index", "frame", "sample", "time", 'raw Pos', "Pos", 'raw Vel', 'Vel', 'raw Acc', 'Acc'])

dt = df["time"][1] - df["time"][0]
num_vel = np.cumsum(df['Acc']) * dt + df['Vel'][0]
start_plot = 150
end_plot = 450

fig, axs= plt.subplots(nrows=3, ncols=1)

axs[0].plot(df['time'][start_plot : end_plot], df['Pos'][start_plot : end_plot], color = 'blue')
axs[0].set_ylabel('Weg (m)')

axs[1].plot(df['time'][start_plot : end_plot], df['Vel'][start_plot : end_plot], color = 'orange')
axs[1].set_ylabel(r'Geschwindigkeit (m $s^{-1}$)')

axs[2].plot(df['time'][start_plot : end_plot], df['Acc'][start_plot : end_plot], color = 'red')
axs[2].set_ylabel(r'Beschleunigung (m $s^{-2}$)')
axs[2].set_xlabel('Zeit (s)')
axs[2].axhline(0, color = 'black' ,linewidth = 0.75,linestyle = '--')

axs[0].xaxis.set_minor_locator(MultipleLocator(.25))
axs[1].xaxis.set_minor_locator(MultipleLocator(.25))
axs[2].xaxis.set_minor_locator(MultipleLocator(.25))

axs[0].yaxis.set_major_locator(MultipleLocator(.3))
axs[1].yaxis.set_major_locator(MultipleLocator(.25))
axs[2].yaxis.set_major_locator(MultipleLocator(2))

axs[0].yaxis.set_minor_locator(MultipleLocator(.15))
axs[1].yaxis.set_minor_locator(MultipleLocator(.125))
axs[2].yaxis.set_minor_locator(MultipleLocator(1))

fig.tight_layout()


#plt.show()

fig1, axs1= plt.subplots(nrows=2, ncols=1)

axs1[0].plot(df['time'][start_plot : end_plot], df['Vel'][start_plot : end_plot], color = 'orange')
axs1[0].set_ylabel(r'Gemessene Gesch. (m $s^{-1}$)')

axs1[1].plot(df['time'][start_plot : end_plot], num_vel[start_plot : end_plot], color = 'red')
axs1[1].set_ylabel(r'Numerische Gesch. (m $s^{-1}$)')
axs1[1].set_xlabel('Zeit (s)')

axs1[0].xaxis.set_minor_locator(MultipleLocator(.25))
axs1[1].xaxis.set_minor_locator(MultipleLocator(.25))

axs1[0].yaxis.set_major_locator(MultipleLocator(.25))
axs1[1].yaxis.set_major_locator(MultipleLocator(.25))

axs1[0].yaxis.set_minor_locator(MultipleLocator(.125))
axs1[1].yaxis.set_minor_locator(MultipleLocator(.125))


fig1.tight_layout()
plt.rcParams.update({"font.size": 20})
plt.show()