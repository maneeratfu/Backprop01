import numpy as np
import math
import readData as rd
import assign_func as func

###config paramiter
p = 0.001
weight = rd.weigth
data = rd.data
output_data = rd.output_design
design = rd.design
epoch = 10

for e in range(epoch):
    arr_y = []
    cost = []
    matrix_cls = [[0, 0], [0, 0]]  #config >>>>>>>>> matrix_cls
    ##feed forward
    for k in range(len(data)):
        arr_y.append([])
        sum_cost = 0
        idx_y = 0
        tmp = [0,0] #config >>>>>>>> tmp,0
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
                    #tmp[2] = tmp[2] + ((y - design[2][i]) ** 2)  #config

            if sum_cost != 0: cost.append(sum_cost * 0.5)

        #classify data
        cls = [math.sqrt(tmp[0]), math.sqrt(tmp[1])]  #config
        classify = func.minimum(cls, len(cls))
        result = func.classify_2class(output_data[k][0],output_data[k][1],classify) #config
        matrix_cls[result[0]][result[1]] +=1

    print("cost >>>",sum(cost))

    if sum(cost) <= 0.5 or e == (epoch-1):
        break
    else:
        arr_s = []
        for k in range(len(arr_y)): #lenght y
            arr_s.append([])
            for x in range(len(weight)-1,-1,-1): #layer
                index = 0
                idx_s = len(arr_s[k])
                for cal in range(x): #calculate to find index y from output layer
                    index = index + len(weight[cal])
                for i in range(len(weight[x])): #node
                    sum_e = 0
                    for j in range(len(weight[x]) if (x+1) == len(weight) else len(weight[x+1]) ): #calculate(sum) to find e values
                        if (x+1) == len(weight):
                            sum_e = sum_e + (arr_y[k][index+j]-output_data[k][j])
                        else:
                            sum_e = sum_e + (arr_s[k][(idx_s-(len(weight[x+1]))+j)] * weight[x+1][j][i+1])
                    s = sum_e * (1 - (arr_y[k][index+i] ** 2))
                    arr_s[k].append(s)
        ##update weight
        idx_s = 0
        for x in range(len(weight)-1,-1,-1):
            index = 0
            if x != 0:
                for cal in range(x-1):  # calculate to find index y from output layer
                    index = index + len(weight[cal])
            for j in range(len(weight[x])): #compute w of node in layer (x)
                c = 0
                for idx_w in range(len(weight[x][j])):
                    sum_w = 0
                    for n in range(len(arr_y)):
                        if x == 0:
                            sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else data[n][c-1]))
                        else:
                            sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else arr_y[n][index + c - 1]))
                    w = weight[x][j][idx_w] + ((-p) * sum_w)
                    weight[x][j][idx_w] = w
                    c+=1
                idx_s+=1

import Testdata as testdata
print(testdata.classifyData(weight))

