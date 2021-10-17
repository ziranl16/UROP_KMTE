import numpy as np
import json
import matplotlib.pyplot as plt


YEARMIN = '-50'
YEARMAX = '3000'


def cal_variance():
    dataset_path = 'data/' + 'yago' + '/' + 'large' + '/train.txt'
    variance_path = 'data/' + 'yago' + '/' + 'large' + '/variance.txt'
    total = {}
    variance = {}
    with open(dataset_path, 'r') as filein:
        for line in filein:
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
            # print("start: {0}, end = {1}".format(start, end))
            relation = int(line.split()[1].strip())
            if relation in total and int(end) - int(start) != 2 and int(end) - int(start) != 1:
                times = total.get(relation)
                times.append(int(end) - int(start))
                # print(int(end) - int(start))
            elif int(end) - int(start) != 2 and int(end) - int(start) != 1:
                times = [int(end) - int(start)]
                #print(int(end) - int(start))
                total[relation] = times

    for key, value in total.items():
        variance[key] = float(np.std(value))

    print(total.get(9))
    # plt.hist(total.get(9))
    # plt.show()

    with open(variance_path, 'w') as file:
        file.write(json.dumps(variance))  # use `json.loads` to do the reverse


if __name__ == "__main__":
    cal_variance()



