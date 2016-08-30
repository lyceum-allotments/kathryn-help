import matplotlib.pyplot as plt
import math
import numpy as np
# import use_tex_font as utf
import matplotlib
import pickle

# utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (4, 3))


x = [0, 6]
y = [0, 0]
plt.plot(x,y, 'k--')

x = np.arange(0.05,20.5, 0.01)
y = [(1 - math.exp(1 - xi))**2 - 1 for xi in x]

plt.plot(x,y)

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

plt.xlabel('$a r$')
plt.ylabel('$\mathrm{V}/D_e$')
fig.subplots_adjust(left=0.15)
ax.set_ylim([-1.0, 2.0])
ax.set_xlim([0.1, 6])
plt.savefig("morse_plot.png", bbox_inches = 'tight', dpi=200) 
# plt.show()
