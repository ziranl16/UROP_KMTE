import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter


# Useful for printing plots in Jupyter

# calculate survival function for worksAt
def survival_find_0(filename):
    relation = "0"
    train_triples = []
    triple_time = np.array([[0, 0]])
    with open(filename, 'r') as filein:
        for line in filein:
            if line.split()[1].strip() == relation:
                train_triples.append([int(x.strip()) for x in line.split()[0:3]])
                start = line.split()[3].split('-')[0]
                end = line.split()[4].split('-')[0]
                if start.isdigit() and end.isdigit() and int(end) >= int(start):
                    if int(end) < int(start):
                        print(start)
                        print(end)
                        print([int(x.strip()) for x in line.split()[0:3]])
                    start = int(start)
                    end = int(end)
                    triple_time = np.append(triple_time, np.array([[0, 0]]), axis=0)
                    triple_time = np.append(triple_time, np.array([[end - start, 1]]), axis=0)
                    # triple_time.append([x.split('-')[0] for x in line.split()[3:5]])
                    # print(triple_time)
        df = pd.DataFrame({'T': triple_time[:, 0], 'E': triple_time[:, 1]})
        T = df['T']
        E = df['E']
        kmf = KaplanMeierFitter()
        kmf.fit(T, E)
        #print(dict)
        # kmf.cumulative_density_
        kmf.plot()
        plt.title("Kaplan Meier estimates relation " + relation)
        plt.xlabel("Years after relation 0")
        plt.ylabel("Survival")
        plt.show()
        print(kmf.survival_function_at_times(39))
        # Plot cumultative density
        kmf.plot_cumulative_density()
        kmf.cumulative_density_.head()
        file_name = relation + '_relation.json'
        kmf.survival_function_.to_json(file_name)
        # with open(file_name, 'w') as fp:
        #     json.dump(kmf.survival_function_.tojs, fp)

if __name__ == '__main__':
    survival_find_0("data/yago/large/train.txt")
