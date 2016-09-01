import matplotlib.pyplot as plt
import math
import numpy as np
import use_tex_font as utf
import matplotlib
import pickle
import itertools

utf.use_tex_font()
matplotlib.rcParams.update({'font.size':9})

fig, ax=plt.subplots(figsize = (2.74, 6.05))

fp = open("results.pckl")
results = pickle.load(fp)

results.sort(lambda a, b : 1 if a["std_order"] > b["std_order"] else -1)
std_order_grouped_results = []
for k, g in itertools.groupby(results, lambda a : a["std_order"]):
    gl = list(g)
    std_order_grouped_results.append({"number_of_structs" : gl[0]["number_of_structs"], "E_min" : min([r["E_min"] for r in gl])})

data = [[],[],[],[]] # data[0] will contain all energies of runs with T_reduced = 0.001,
                  # data[1] with T_reduced = 0.01, data[2] with T_reduced = 0.1, data[3] with T_reduced = 1.0 
num_structures_lookup = {1 : 0, 2 : 1, 4 : 2, 8 : 3}

for r in std_order_grouped_results:
    index = num_structures_lookup[r["number_of_structs"]]
    data[index].append(r["E_min"])

plt.boxplot(data, whis = 200)
ax.set_xticklabels([1, 2 ,4, 8])

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

plt.xlabel('$N_{\mathrm{structures}}$')
plt.ylabel('$E_{min}$')
fig.subplots_adjust(left=0.15)
plt.savefig("E_final_vs_num_structures.png", bbox_inches = 'tight', dpi=200) 
# plt.show()
