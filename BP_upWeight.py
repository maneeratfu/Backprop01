import numpy as np
weigth = {
    0: [
        [-0.2, 0.1, 0.5],
        [-1, 0.8, 0.6],
        [0.7, -0.5, 0.4]
    ],
    1: [
        [0.3, 0.1, 0.2, 0.2],
        [1, -0.5, -0.2, 0.7]
    ],
    2: [
        [0.5, 0.2, -0.5],
        [0.5, 0.1, 0.1]
    ]
}
p=0.1
data = np.array([[0.7, 0.6], [-0.4, -0.1], [-0.2, -0.5], [1.2, 2.3]])
output_data = np.array([[0.9,0.1],[0.1,0.9],[0.1,0.9],[0.9,0.1]])
arr = [
    [1.1,1.2,1.3,1.4,1.5,1.6,1.7 ],
    [2.1,2.2,2.3,2.4,2.5,2.6,2.7 ],
    [3.1,3.2,3.3,3.4,3.5,3.6,3.7 ],
    [4.1,4.2,4.3,4.4,4.5,4.6,4.7 ],
]
arr_s = []
l = len(weigth)
count = 0

##update weight
idx_s = 0
for x in range(len(weigth)-1,-1,-1):
    index = 0
    #print("layer %d" %(x+1))
    if x != 0:
        for cal in range(x-1):  # calculate to find index y from output layer
            index = index + len(weigth[cal])
    for j in range(len(weigth[x])): #compute w of node in layer (x)
        #print("node %d" %(j+1))
        c = 0
        for idx_w in range(len(weigth[x][j])):
            sum_w = 0
            for n in range(len(arr)):
                if x == 0:
                    sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else data[n][c-1]))
                    #print(arr_s[n][idx_s], "x", (1 if idx_w == 0 else data[n][c-1]))
                else:
                    sum_w = sum_w + (arr_s[n][idx_s] * (1 if idx_w == 0 else arr[n][index + c - 1]))
                    #print(arr_s[n][idx_s], "x", (1 if idx_w == 0 else arr[n][index+c-1]))
            #print(">>>", weigth[x][j][idx_w] if x!=0 else "")
            w = weigth[x][j][idx_w] + ((-p) * sum_w)
            weigth[x][j][idx_w] = w
            c+=1
        idx_s+=1
    #print("--------------------")
idx_s = 0