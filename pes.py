import numpy as np
import math

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()

fig =plt.figure(figsize = (6, 5))
ax = fig.add_subplot(111, projection='3d')

rangea = np.arange(0.0,8.0, 0.3)

X = np.empty([len(rangea), len(rangea)])
Y = np.empty([len(rangea), len(rangea)])
Z = np.empty([len(rangea), len(rangea)])

for i_x, x in enumerate(rangea):
    for i_y, y in enumerate(rangea):
        X[i_x][i_y] = x
        Y[i_x][i_y] = y
        Z[i_x][i_y] = (y* math.sin(x) + (y+3)/1.01*math.cos(y))

ax.view_init(54, -37)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.GnBu)
# ax.set_xlabel("Li/Mg Swap ratio")
# ax.set_ylabel("log_10 (reduced T) ")
ax.set_zlabel("V")
plt.savefig("pes_plot.png", dpi=200)
