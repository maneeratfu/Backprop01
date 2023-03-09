import numpy as np
input_file = open("train_data/Centerinput.txt", "r")
input_data = [(line.strip()).split() for line in input_file]
input_file.close()

output_file = open("train_data/Centeroutput.txt", "r")
output_data = [(line.strip()).split() for line in output_file]
output_file.close()

design_class = [
    [[0,9,0.1,0.1],[0.1,0.9,0.1],[0.1,0.1,0.9]],
    [[0.9,0.1],[0.1,0.9]]
]
data = []
for i in range(len(input_data)):
    data.append([])
    for x in input_data[i]:
        a = x.split(",")
    for add_a in range(len(a)):
        data[i].append(a[add_a])
    data[i] = [float(x) for x in data[i]]
output_design = []
for i in range(len(output_data)):
    output_design.append([])
    for x in output_data[i]:
        a = x.split(",")
    for add_a in range(len(a)):
        output_design[i].append(a[add_a])
    output_design[i] = [float(x) for x in output_design[i]]

data = np.array(data)
output_design = np.array(output_design)
#config
design = design_class[1] #ถ้า3เปลี่ยนเลข0
Layer = [3,2,len(output_design[0])]
weigth = []
for x in range(len(Layer)):
    if x == 0:
        size = (3, (len(data[0])+1))
        k = np.random.uniform(-1, 1, size)
        weigth.append(k)
    else:
        size = (Layer[x], (Layer[x-1]+1))
        k = np.random.uniform(-1, 1, size)
        weigth.append(k)
