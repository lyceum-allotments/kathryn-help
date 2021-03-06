import matplotlib.pyplot as plt
import math
import numpy as np
import use_tex_font as utf
import matplotlib
import pickle

utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (2.74, 6.05))

fp = open("results.pckl")
results = pickle.load(fp)

data = [[],[],[],[]] # data[0] will contain all energies of runs with T_reduced = 0.001,
                  # data[1] with T_reduced = 0.01, data[2] with T_reduced = 0.1, data[3] with T_reduced = 1.0 
max_step_lookup = {100 : 0, 500 : 1, 1000 : 2, 2000 : 3}

for r in results:
    index = max_step_lookup[r["max_steps"]]
    data[index].append(r["E_min"])

plt.boxplot(data, whis = 200)
ax.set_xticklabels([100, 500, 1000, 2000])

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

plt.xlabel('$T_{r}$')
plt.ylabel('$E_{min}$')
fig.subplots_adjust(left=0.15)
plt.savefig("E_final_vs_max_steps.png", bbox_inches = 'tight', dpi=200) 
# plt.show()
