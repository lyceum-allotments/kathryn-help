import matplotlib.pyplot as plt
import pickle

fp = open("results.pckl")
results = pickle.load(fp)
graph_formats = {100: {'fmt' : 'v', 'color' : '#ff0000'},
        500: {'fmt' : '+', 'color' : '#00ff00'},
        1000: {'fmt' : 'D', 'color' : '#0000ff'},
        2000: {'fmt' : 'x', 'color' : '#000000'}}

def plot_E_initial_vs_E_final(max_steps):
    E_initial_series = []
    E_final_series = []
    plot_results = filter(lambda x : (int(x["max_steps"]) == max_steps), results)

    for p in plot_results:
        E_initial_series.append(p["E_min_step"][0])
        E_final_series.append(p["E_min"])

    plt.plot(E_initial_series, E_final_series, graph_formats[max_steps]['fmt'], fillstyle='none', ms=8, markeredgewidth=2, label = "%d steps" % max_steps, color = graph_formats[max_steps]['color'])

for total_steps in [100, 500, 1000, 2000]:
    plot_E_initial_vs_E_final(total_steps)

plt.xlabel('E initial (eV)')
plt.ylabel('E final (eV)')
plt.legend(numpoints=1)
plt.show()
