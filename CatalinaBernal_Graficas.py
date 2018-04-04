import numpy as np
import matplotlib.plyplot as plt

datp = np.loadtxt('times_python.csv, delimiter = ',')
datc = np.loadtxt('times_cpp.csv', delimiter = ',')

tiempo1 = datp[:,1]
tiempo2 = datc[:,1]
N = datp[:,0]

plt.figure()
plt.plot(N, tiempo1, label = 'Tiempo Python')
plt.plot(N, tiempo2, label = 'Tiempo C++')
plt.xlabel('N')
plt.ylabel('Tiempo')
plt.title('Cpp  vs. Python')
plt.legend()
plt.savefig('cpp_vs_python.png')
