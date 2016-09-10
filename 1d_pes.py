import matplotlib.pyplot as plt
import math
import numpy as np
import use_tex_font as utf
import matplotlib
import pickle
import matplotlib.patches

def f(x):
    """ function for 1D-potential surface"""
    return (math.sin(x*(2*math.pi)/2.) + 1) * (0.097 * x**2 + -0.30555*x + 0.90625) - (x - 3.5)

# utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (4, 3))

x = np.arange(0.85,5.0, 0.05)
y = [f(xi) for xi in x]
# y = [4 * ((1/xi)**12. - (1/xi)**6.) for xi in x]

plt.plot(x,y)


# adding arrows
for p1, p2 in [((4.31, 1.90), (4.04, 0.979)),
               ((4.01, 0.886), (3.85, 0.393)),
               ((3.84, 0.323), (3.62, 0)) 
               ]:
    arr = matplotlib.patches.FancyArrowPatch(p1, p2, connectionstyle='arc3, rad=0.6', mutation_scale=20, arrowstyle='-|>', fc='k')
    ax.add_patch(arr)

# adding points
x = [4.36, 4.06, 3.89, 3.62]
y = [f(xi) for xi in x]

plt.plot(x,y, 'ko', ms = 4.0)

plt.text(4.4, 1.8, "1", verticalalignment = "top")
plt.text(4.12, 0.914, "2", verticalalignment = "top")
plt.text(3.95, 0.365, "3", verticalalignment = "top")
plt.text(3.655, -0.155, "4", verticalalignment = "top")

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

fig.subplots_adjust(left=0.15)
ax.set_ylim([-1, 4])
ax.set_xlim([0, 5.5])
plt.savefig("1d_pes_plot.png", bbox_inches = 'tight', dpi=200) 
# plt.show()
