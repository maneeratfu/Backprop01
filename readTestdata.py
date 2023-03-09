import numpy as np
input_file = open("test_data/Centerinputtest.txt", "r")
input_data = [(line.strip()).split() for line in input_file]
input_file.close()

output_file = open("test_data/Centeroutputtest.txt", "r")
output_data = [(line.strip()).split() for line in output_file]
output_file.close()

design_class = [
    [[0,9,0.1,0.1],[0.1,0.9,0.1],[0.1,0.1,0.9]],
    [[0.9,0.1],[0.1,0.9]],[[0.9,0.9,0.9,0.1,0.1,0.1],[0.1,0.9,0.9,0.1,0.1],[0.1,0.1,0.9,0.9,0.9,0.1],[0.1,0.1,0.1,0.9,0.9,0.9],[0.9,0.1,0.1,0.1,0.9,0.9],[0.9,0.9,0.1,0.1,0.1,0.9]]
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
design = design_class[1]
