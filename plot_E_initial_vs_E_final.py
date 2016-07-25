import matplotlib.pyplot as plt
import pickle

fp = open("results.pckl")
results = pickle.load(fp)

E_initial_series = []
E_final_series = []

for r in results:
    E_initial_series.append(r["E_min_step"][0])
    E_final_series.append(r["E_min"])

plt.plot(E_initial_series, E_final_series, 'bo')
plt.xlabel('E initial (eV)')
plt.ylabel('E final (eV)')
plt.show()
