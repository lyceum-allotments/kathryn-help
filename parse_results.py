import os
import pickle

def parse_submit_file(fpath):
    """ parses submit file at 'fpath', getting the parameters for the calculation.
 returns tuple of max_steps, swap_freq, T_reduced."""
    fp = open(fpath, "r")

    for l in fp.readlines():
        if l.find("do_monte_carlo_multi_swap.py") != -1:
            lsplit = l.split()
            max_steps, swap_freq, T_reduced = lsplit[2:]
            swap_freq = [float(i) for i in swap_freq[1:-1].split(":")]
            swap_freq = swap_freq[0] / swap_freq[1]
            return int(max_steps), swap_freq, float(T_reduced)

def parse_output_file(fpath):
    """ parses the output file at 'fpath' and returns tuple
 containing accepted_steps, mc_rejected_steps, convergence_rejected_steps."""
    e_accepted_steps = 0
    mc_accepted_steps = 0
    mc_rejected_steps = 0
    convergence_rejected_steps = 0
    for l in open(fpath).readlines():
        if l.find("SGE job") >= 0:
            e_accepted_steps = 0
            mc_accepted_steps = 0
            mc_rejected_steps = 0
            convergence_rejected_steps = 0
        if l.find("E accept") >= 0:
            e_accepted_steps += 1
        elif l.find("MC accept") >= 0:
            mc_accepted_steps += 1
        elif l.find("MC reject") >= 0:
            mc_rejected_steps += 1
        elif l.find("Convergence reject") >= 0:
            convergence_rejected_steps += 1
    return (e_accepted_steps, mc_accepted_steps, mc_rejected_steps, convergence_rejected_steps)

def load_energies_pckl(fpath):
    fp = open(fpath, "r")
    energies, images = pickle.load(fp)
    return list(energies)

def get_step_and_E_min(energies):
    """ get the minimum energy from a list of energies, and the step it occured at."""
    if len(energies) == 0:
        print "no results in pckl file!!"
        return [0, 0.0]
    
    energies_sorted = zip(range(len(energies)), energies[:])
    
    energies_sorted.sort(lambda a, b : 1 if a[1] > b[1] else -1)

    return energies_sorted[0]

def get_e_min_step(energies):
    """ get a list of minimum energies from each step of a calculation."""
    e_min_step = []

    for i, e in enumerate(energies):
        e_trunc = energies[:i+1]
        e_trunc.sort()
        e_min_step.append(e_trunc[0])

    return e_min_step

# array of results, each result will be a dict with the following keys:
# "std_order"         : number signifying unique combination of (steps, frequencies,
#                           reduced T, and number of initial structs)
# "number_of_structs" : how many starting structures were used in the calculation
# "struct_index"      : the index of the structure
# "max_steps"         : max number of steps of calculation
# "swap_freq"         : Li/Mg swap frequency
# "T_reduced"         : reduced temperature
# "E_min"             : minimum energy reached during MC calculation
# "min_step:          : step that minimum energy was reached
# "E_min_step"        : list containing minimum energy at each step of MC calculation
# "E_accepted_steps"           : E_accepted_steps,
# "MC_accepted_steps"          : MC_accepted_steps,
# "MC_rejected_steps"          : MC_rejected_steps,
# "convergence_rejected_steps" : convergence_rejected_steps,
# 
results = []
std_order_number_of_structs_map = {}

for root, dirs, files in os.walk("."):
    split_root = root.split("/")
    if len(split_root) == 3:
        try:
            std_order = int(split_root[1])
            struct_index = int(split_root[2])
        except ValueError: 
            continue

        if "submit" in files:
            max_steps, swap_freq, T_reduced = parse_submit_file(root + "/submit")
        else:
            print "no submit script in %s!!" % root

        if "output.txt" in files:
            E_accepted_steps, MC_accepted_steps, MC_rejected_steps, convergence_rejected_steps = parse_output_file(root + "/output.txt")
        else:
            print "no output.txt in %s!!" % root
            E_accepted_steps, MC_rejected_steps, convergence_rejected_steps = (0,0,0)
        total_steps =  E_accepted_steps + MC_accepted_steps + MC_rejected_steps + convergence_rejected_steps

        if total_steps != max_steps:
            raise Exception("total steps != max_steps, something inconsistent, stdOrder: %d, struct index %d, total_steps %d, max_steps %d" % (std_order, struct_index, total_steps, max_steps))

        if "energies_images.pckl" in files: # in structure directory
            all_energies = load_energies_pckl(root + "/energies_images.pckl")
            min_step, E_min = get_step_and_E_min(all_energies)
            E_min_step = get_e_min_step(all_energies)
        else:
            print "no results in %s!!" % root
            min_step, E_min, E_min_step = (0,0,[0])
        
        results.append({
            "std_order"                  : std_order,
            "number_of_structs"          : 0, # done later
            "struct_index"               : struct_index,
            "max_steps"                  : max_steps,
            "swap_freq"                  : swap_freq,
            "T_reduced"                  : T_reduced,
            "E_min"                      : E_min,
            "min_step"                   : min_step,
            "E_min_step"                 : E_min_step,
            "E_accepted_steps"           : E_accepted_steps,
            "MC_accepted_steps"          : MC_accepted_steps,
            "MC_rejected_steps"          : MC_rejected_steps,
            "convergence_rejected_steps" : convergence_rejected_steps,
            })

        if std_order_number_of_structs_map.has_key(std_order):
            std_order_number_of_structs_map[std_order] += 1
        else:
            std_order_number_of_structs_map[std_order] = 1

for r in results:
    r["number_of_structs"] = std_order_number_of_structs_map[r["std_order"]]

fp = open("results.pckl", "w")
pickle.dump(results, fp)
