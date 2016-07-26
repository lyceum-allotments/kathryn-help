import matplotlib.pyplot as plt
import pickle

fp = open("results.pckl")
results = pickle.load(fp)
graph_formats = {100: 'rv', 500: 'b+', 1000: 'gD', 2000: 'kx'}

def plot_E_initial_vs_E_final(max_steps):
    E_initial_series = []
    E_final_series = []
    plot_results = filter(lambda x : (int(x["max_steps"]) == max_steps), results)

    for p in plot_results:
        E_initial_series.append(p["E_min_step"][0])
        E_final_series.append(p["E_min"])

    plt.plot(E_initial_series, E_final_series, graph_formats[max_steps], fillstyle='none', ms=8, markeredgewidth=2, label = "%d steps" % max_steps)

for total_steps in [100, 500, 1000, 2000]:
    plot_E_initial_vs_E_final(total_steps)

plt.xlabel('E initial (eV)')
plt.ylabel('E final (eV)')
plt.legend()
plt.show()
