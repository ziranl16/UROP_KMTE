import numpy as np
import json
import matplotlib.pyplot as plt

YEARMIN = '-50'
YEARMAX = '3000'


def filter_durations():
    target_path = 'data/' + 'yago' + '/' + 'large' + '/valid.txt'

    with open(target_path, "r") as f:
        lines = f.readlines()

    with open(target_path, "w") as f:
        for line in lines:
            sttrr = line.strip("\n")
            #print(sttrr)
            arr = sttrr.split('\t')

            # if int(arr[1]) != 0 and int(arr[1]) != 7:
            #     print(arr[1])
            #     f.write(line)

            if int(arr[1]) == 8:
                arr[1] = '0'
                temp = ''
                for c in arr:
                    temp = temp + c + '\t'
                print(temp)
                f.write(temp)
            elif int(arr[1]) == 9:
                arr[1] = '7'
                temp = ''
                for c in arr:
                    temp = temp + c + '\t'
                print(temp)
                f.write(temp)
            else:
                f.write(line)


if __name__ == "__main__":
    filter_durations()
