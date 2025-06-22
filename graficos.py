import matplotlib.pyplot as plt
import numpy as np

universidades = ["UTDT", "MIT", "Cambridge", "UTS"]
distancia = np.array([12, 8650, 11190, 11800, 14900])
avgRTT = np.array([2.59, 4.43, 5.18, 5.67, 5.80])
# maxRTTs = 

# Grafico RTTs
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(distancia, avgRTT)  # Plot some data on the Axes.
ax.yaxis.set_major_formatter
plt.xlabel("Distancia (en km)")
plt.ylabel("Avg. RTT")
plt.show()    