import numpy as np
import math
import importData as imd
'''weight = [
    [[-0.2,0.1,0.5],[-1,0.8,0.6],[0.7,-0.5,0.4]],
    [[0.3,0.1,0.2,0.2],[1,-0.5,-0.2,0.7]],
    [[0.5,0.2,-0.5],[0.5,0.1,0.1]]
]'''
weight = imd.weigth
p = 0.01
data = imd.data
output_data = imd.output_design
arr_y = []
cost = []
##feed forward
for k in range(len(data)):
    arr_y.append([])
    sum_cost = 0
    idx_y = 0
    for x in range(len(weight)):  # fetch weigth of Layer
        if (x + 1) != 1:
            idx_y = ((x - 1) * len(weight[x - 1])) + (x - 1)
        for i in range(len(weight[x])):  # fetch weigth
            sum_v = 0
            c = idx_y
            for j in range(len(weight[x][i])):  # sum v to y values
                if (x + 1) == 1:
                    sum_v = sum_v + (weight[x][i][j] * (1 if j == 0 else data[k][j - 1]))
                else:
                    sum_v = sum_v + (weight[x][i][j] * (1 if j == 0 else arr_y[k][c]))
                    if j != 0:
                        c += 1

            y = 1 / (1 + math.exp(-sum_v))
            arr_y[k].append(y)

            if (x + 1) == len(weight):  # calculate cost of output layer
                sum_cost = sum_cost + ((y - output_data[k][i]) ** 2)

        if sum_cost != 0: cost.append(sum_cost * 0.5)

print(sum(cost))
print(arr_y)
