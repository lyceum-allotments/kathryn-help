# Plots colourmap of E_min(f, T_r) (average minimum energy of 2000 step calculations
# as a function of swap frequency and reduced temperature)

import pickle
import numpy as np
import math
import matplotlib.pyplot as plt

fp = open("results.pckl")
results = pickle.load(fp)

# only look at results with 2000 steps
results = filter(lambda x : (int(x["max_steps"]) == 2000), results)

# only look at results with 8 starting structures
results = filter(lambda x : (int(x["number_of_structs"]) == 8), results)

# sort results by energy (ascending)
results.sort(lambda x, y : -1 if (float(x["E_min"]) < float(y["E_min"])) else 1)

# find reference energy
E_ref = float(results[0]["E_min"])

E_min = {}
for r in results:
    try:
        E_min[r["reduced_T"]][r["swap_freq"]] = (r["energy"] - E_ref) / r["number_of_structs"]
    except KeyError:
        E_min[r["reduced_T"]] = {}
        E_min[r["reduced_T"]][r["swap_freq"]] = (r["energy"] - E_ref) / r["number_of_structs"]

reduced_Ts = E_min.keys()
reduced_Ts.sort()

swap_frequencies = E_min[reduced_Ts[0]].keys()
swap_frequencies.sort()

E_min_grid = np.empty([len(reduced_Ts),len(swap_frequencies)])
reduced_T_grid = np.empty([len(reduced_Ts),len(swap_frequencies)])
swap_frequencies_grid = np.empty([len(reduced_Ts),len(swap_frequencies)])

for i_T, T in enumerate(reduced_Ts):
    for i_f, f in enumerate(swap_frequencies):
        reduced_T_grid[i_T][i_f] = math.log(T, 10)
        swap_frequencies_grid[i_T][i_f] = f
        E_min_grid[i_T][i_f] = E_min[T][f]

plt.pcolor(swap_frequencies_grid, reduced_T_grid, E_min_grid, cmap="RdBu")
plt.colorbar()
plt.xlabel("Li/Mg Swap ratio")
plt.ylabel("log_10 (reduced T)")
