import numpy as np
import matplotlib.pyplot as plt
def f(t): return (t)+1997
t1 = np.arange(0.0, 20.0, 1)
plt.plot(t1, f(t1), 'r--o', linewidth = 2.5)
plt.xlabel('Edad')
plt.ylabel('Anio')
plt.title('Humberto Vazquez Castro', fontsize = 30)
plt.savefig('edad.png')
plt.show()
