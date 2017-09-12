import numpy as np
import matplotlib.pyplot as plt
def f(t): return (t)+1997
def g(t): return 3*np.cos(2*np.pi*t)+2014
t1 = np.arange(0.0, 20.0, 1)
t2 = np.arange(0.0, 5.0, 0.01)
plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'b--*', t2, g(t2), 'k:', linewidth = 4)
plt.subplot(212)
plt.plot(t2, 3*np.cos(2*np.pi*t2)+2014, 'r--D')
plt.savefig('2graf.png')
plt.show()
