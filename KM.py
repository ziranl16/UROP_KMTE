import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

YEARMIN = -50
YEARMAX = 3000


# Useful for printing plots in Jupyter

# calculate survival function for worksAt
def survival_find_0(filename):
    r = "3"
    triple_time = np.array([[0, 0]])
    with open(filename, 'r') as filein:
        for line in filein:
            relation = line.split()[1].strip()
            start = line.split()[3].split('-')[0]
            end = line.split()[4].split('-')[0]
            if start == '####':
                start = YEARMIN
            elif start.find('#') != -1 or len(start) != 4:
                continue

            if end == '####':
                end = YEARMAX
            elif end.find('#') != -1 or len(end) != 4:
                continue

            start = int(start)
            end = int(end)

            if start > end:
                end = YEARMAX

            if end >= start:
                if relation == r:
                    triple_time = np.append(triple_time, np.array([[0, 0]]), axis=0)
                    triple_time = np.append(triple_time, np.array([[end - start, 1]]), axis=0)

        df = pd.DataFrame({'T': triple_time[:, 0], 'E': triple_time[:, 1]})
        T = df['T']
        E = df['E']
        kmf = KaplanMeierFitter()
        kmf.fit(T, E)

        kmf.plot()
        plt.title("Kaplan Meier estimates relation <isMarriedTo>")
        plt.xlabel("Years after relation <isMarriedTo>")
        plt.ylabel("Survival Rate")
        plt.xlim(0, 30)
        plt.show()
        p = kmf.survival_function_at_times(3).values[0]
        print(p)


if __name__ == '__main__':
    survival_find_0("data/yago/large/train.txt")
