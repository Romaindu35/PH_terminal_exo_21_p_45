import matplotlib.pyplot as plt
import numpy as np

x = [10.0, 7.5, 5.0, 2.5, 1.0]
y = [5.88, 4.41, 2.94, 1.47, 0.59]

modele = np.polyfit(x,y,1)

plt.title("Graphique d'étalonage avec G = " + str(modele[0])[:5] + " x C")
plt.xlabel("C (mmol/L)")
plt.ylabel("G (mS)")
plt.plot(x, y, "bo", label="points\\expérimentaux")
plt.axis(xmin=0, xmax=10, ymin=0, ymax=6)
plt.grid(linestyle="-.")
plt.xticks(range(11))


print(modele)

plt.show()
