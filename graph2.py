
import matplotlib.pyplot as plt
import numpy as np

# إنشاء القيم
x = np.linspace(0, 10, 100)
y = x**2

# رسم المنحنى
plt.plot(x, y)

# عنوان
plt.title("$y = x^2$")

# حفظ الصورة
plt.savefig("/storage/emulated/0/Download/graphe2.png")
