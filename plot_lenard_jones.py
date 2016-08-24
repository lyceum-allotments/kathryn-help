import matplotlib.pyplot as plt
import math
import numpy as np
import use_tex_font as utf
import matplotlib
import pickle

utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (4, 3))


x = [0, 2.5]
y = [0, 0]
plt.plot(x,y, 'k--')

x = np.arange(0.85,2.5, 0.01)
y = [4 * ((1/xi)**12. - (1/xi)**6.) for xi in x]

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

plt.xlabel('$\mathrm{V}/\epsilon$')
plt.ylabel('$r/\sigma$')
fig.subplots_adjust(left=0.15)
ax.set_ylim([-1.2, 5])
ax.set_xlim([0, 2.5])
plt.savefig("lenard_jones_plot.png", bbox_inches = 'tight', dpi=200) 
# plt.show()
