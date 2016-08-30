import matplotlib.pyplot as plt
import math
import numpy as np
# import use_tex_font as utf
import matplotlib
import pickle

def buck(r, include_coulomb):

    epsilon = 1.0 # depth of min
    alpha = 1.0 # dimensionless param
    R_0 = 1.0 # min energy distance
    if include_coulomb:
        return epsilon * (6/(alpha - 6) * math.exp(alpha * (1 - r / R_0)) - alpha/(alpha - 6) * (R_0/r)**6.) - 1/r
    else:
        return epsilon * (6/(alpha - 6) * math.exp(alpha * (1 - r / R_0)) - alpha/(alpha - 6) * (R_0/r)**6.)
# utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (4, 3))

x = [0, 6]
y = [0, 0]
plt.plot(x,y, 'k--')

x = np.arange(0.05,6.0, 0.01)
# y = [math.exp(-xi) - 1/xi**6 - 1/xi for xi in x]
y = [buck(xi, False) for xi in x]

plt.plot(x,y, label = "Buckingham")

x = np.arange(0.05,6.0, 0.01)
# y = [math.exp(-xi) - 1/xi**6 - 1/xi for xi in x]
y = [buck(xi, True) for xi in x]

plt.plot(x,y, label = "Buckingham + Coulomb")

plt.tick_params(\
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on') # labels along the bottom edge are off

plt.tick_params(\
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left='on',      # ticks along the bottom edge are off
    right='off',         # ticks along the top edge are off
    labelbottom='on') # labels along the bottom edge are off

plt.xlabel('$r/r_0$')
plt.ylabel('$\mathrm{V}/\epsilon$')
fig.subplots_adjust(left=0.15)
ax.set_ylim([-2.2, 2.0])
ax.set_xlim([0.1, 6])
plt.legend()
plt.savefig("buckingham_plot.png", bbox_inches = 'tight', dpi=200) 

# plt.show()
