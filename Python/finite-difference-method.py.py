import numpy as np
from time import clock
from math import log

"""
    A primeira parte do programa utiliza o método das diferênças finitas para resolver o Problema:
    d²E/dP² + d²E/dD² = P/D + D/P
    com h = k = 1
    onde m*k = b - a e n*h = d - c, sendo a=1, b=81 e c=1, d=100
"""

m = 80
n = 99
k = h = 1
it = 100

f = lambda P,D: P/D + D/P

p = np.arange((m-1)*(n-1)).reshape(m-1,n-1)
w = np.zeros((m-1)*(n-1))

t1 = clock()
for _ in range(it):
    for i,I in zip(range(m-1),range(m,1,-1)):
        for j in range(n-1):
            J = j+2
            w_i_1 = 162*J*h*log(9*J*h) if i-1 == -1 else w[p[i-1][j]]
            w_i1 = J*h*log(J*h) if i+1 == m-1 else w[p[i+1][j]]
            w_j_1 = I*k*log(I*k) if j-1 == -1 else w[p[i][j-1]]
            w_j1 = 200*I*k*log(10*I*k) if j+1 == n-1 else w[p[i][j+1]]
            w[p[i,j]] = 0.25 * ( w_i_1 + w_i1 + w_j_1 + w_j1 - f(I * k,(j + 2) * h) )
t2 = clock()
print(t2-t1)

"""
    A segunda parte do programa plota o resultado da equação diferêncial
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(2,n+1)
Y = np.arange(m,1,-1)

x,y = np.meshgrid(X,Y)
z = w.reshape(m-1,n-1)

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel("Produzido")
plt.ylabel("Demanda Prevista")

plt.show()
