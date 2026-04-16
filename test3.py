import import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x,y)
plt.axis('equal')  # هاد السطر مهم باش الدائرة تبان صحيحة
plt.xlabel("L'axe X")
plt.ylabel("L'axe Y")
plt.savefig("/storage/emulated/0/Download/test3.png")
plt.grid(True)



