import numpy as np
import matplotlib.pyplot as plt

minimiumFrequency = 1000
maximiumFrequency = 3000

frequency = np.arange(minimiumFrequency, maximiumFrequency, 3)
amplitude = []
for i in range(0,len(frequency)):
  if (i <= len(frequency)/2):
    amplitude.append(i)
  else:
    amplitude.append(len(frequency) - i)

fig, ax = plt.subplots()

ax.fill(frequency, amplitude, 'r',  alpha=0.3)

ax.plot(frequency, amplitude, c='b', alpha=0.8)
plt.title('Bandwidth of a Signal')

plt.show()