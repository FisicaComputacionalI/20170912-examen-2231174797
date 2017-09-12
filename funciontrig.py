import numpy as np
import matplotlib.pyplot as plt
def f(t):return 3*np.cos(2*np.pi*t)+2014
t1 = np.arange(0.0, 5.0, 0.01)
plt.figure(1)
plt.subplot(111)
plt.plot(t1, f(t1), 'm:p')
plt.title('Funcion trigonometrica', fontsize = 45)
plt.savefig('funtrig.png')
plt.show()
