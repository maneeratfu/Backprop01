import numpy as np
import math
weight = [
    [[-0.2,0.1,0.5],[-1,0.8,0.6],[0.7,-0.5,0.4]],
    [[0.3,0.1,0.2,0.2],[1,-0.5,-0.2,0.7]],
    [[0.5,0.2,-0.5],[0.5,0.1,0.1]]
]
p = 0.1
data = np.array([[0.7, 0.6 ], [-0.4, -0.1 ], [-0.2, -0.5 ], [1.2, 2.3 ]])
output_data = np.array([[0.9,0.1 ],[0.1,0.9 ],[0.1,0.9 ],[0.9,0.1 ]])
epoch = 1
for e in range(epoch):
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

    if sum(cost) <= 0.5 or e == epoch:
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
            print(arr_s[k])

        ##update weight
        idx_s = 0
        for x in range(len(weight)-1,-1,-1):
            index = 0
            print("layer %d" %(x+1))
            if x != 0:
                for cal in range(x-1):  # calculate to find index y from output layer
                    index = index + len(weight[cal])
            for j in range(len(weight[x])): #compute w of node in layer (x)
                print("node %d" %(j+1))
                c = 0
                for idx_w in range(len(weight[x][j])):
                    sum_w = 0
                    for n in range(len(arr_y)):
                        if x == 0:
                            sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else data[n][c-1]))
                            print(arr_s[n][idx_s], "x", (1 if idx_w == 0 else data[n][c-1]))
                        else:
                            sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else arr_y[n][index + c - 1]))
                            print(arr_s[n][idx_s], "x", (1 if idx_w == 0 else arr_y[n][index+c-1]))
                    print(">>>", weight[x][j][idx_w])
                    w = weight[x][j][idx_w] + ((-p) * sum_w)
                    weight[x][j][idx_w] = w
                    c+=1
                idx_s+=1
            #print("--------------------")

print(weight)