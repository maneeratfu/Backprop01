import assign_func as func
import readTestdata as rt
import math
import numpy as np
def classifyData (weight):
    data = rt.data
    output_data = rt.output_design
    weight = weight
    design = rt.design
    arr_y = []
    cost = []
    matrix_cls = [[0, 0], [0, 0]]
    ##feed forward
    for k in range(len(data)):
        arr_y.append([])
        sum_cost = 0
        idx_y = 0
        tmp = [0, 0]  # config >>>>>>>> tmp
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
                y = 1 / (1 + np.exp(-sum_v))
                arr_y[k].append(y)
                if (x + 1) == len(weight):  # calculate cost of output layer
                    sum_cost = sum_cost + ((y - output_data[k][i]) ** 2)
                    ##>> sum(tmp) ucledien distance
                    tmp[0] = tmp[0] + ((y - design[0][i]) ** 2)
                    tmp[1] = tmp[1] + ((y - design[1][i]) ** 2)
                    #tmp[2] = tmp[2] + ((y - design[2][i]) ** 2)  # config

            if sum_cost != 0: cost.append(sum_cost * 0.5)

        # classify data
        cls = [math.sqrt(tmp[0]), math.sqrt(tmp[1])]  # config
        classify = func.minimum(cls, len(cls))
        result = func.classify_2class(output_data[k][0], output_data[k][1], classify)  # config
        matrix_cls[result[0]][result[1]] += 1

    return matrix_cls