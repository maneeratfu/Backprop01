def minimum(a, n):
    minpos = a.index(min(a))
    return minpos

def classify_3class(y1,y2,y3,classify):
    if y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and classify == 0:
        return 0,0
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and classify == 1:
        return 0,1
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and classify == 2:
        return 0,2
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.1 and classify == 0:
        return 1,0
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.1 and classify == 1:
        return 1,1
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.1 and classify == 2:
        return 1,2
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and classify == 0:
        return 2,0
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and classify == 1:
        return 2,1
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and classify == 2:
        return 2,2

def classify_2class(y1,y2,classify):
    if y1 == 0.9 and y2 == 0.1 and classify == 0:
        return 0,0
    elif y1 == 0.9 and y2 == 0.1 and classify == 1:
        return 0,1
    elif y1 == 0.1 and y2 == 0.9 and classify == 0:
        return 1,0
    elif y1 == 0.1 and y2 == 0.9 and classify == 1:
        return 1,1

def classify_6class(y1,y2,y3,y4,y5,y6,classify):
    if y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 0:
        return 0,0
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 1:
        return 0,1
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 2:
        return 0,2
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 3:
        return 0,3
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 4:
        return 0,4
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.9 and y4 == 0.1 and y5 == 0.1 and y6 == 0.1 and classify == 5:
        return 0,5



    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 0:
        return 1,0
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 1:
        return 1,1
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 2:
        return 1,2
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 3:
        return 1,3
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 4:
        return 1,4
    elif y1 == 0.1 and y2 == 0.9 and y3 == 0.9 and y4 == 0.9 and y5 == 0.1 and y6 == 0.1 and classify == 5:
        return 1,5



    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 0:
        return 2,0
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 1:
        return 2,1
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 2:
        return 2,2
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 3:
        return 2,3
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 4:
        return 2,4
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.9 and y4 == 0.9 and y5 == 0.9 and y6 == 0.1 and classify == 5:
        return 2,5



    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 0:
        return 3,0
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 1:
        return 3,1
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 2:
        return 3,2
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 3:
        return 3,3
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 4:
        return 3,4
    elif y1 == 0.1 and y2 == 0.1 and y3 == 0.1 and y4 == 0.9 and y5 == 0.9 and y6 == 0.9 and classify == 5:
        return 3,5



    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 0:
        return 4,0
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 1:
        return 4,1
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 2:
        return 4,2
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 3:
        return 4,3
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 4:
        return 4,4
    elif y1 == 0.9 and y2 == 0.1 and y3 == 0.1 and y4 == 0.1 and y5 == 0.9 and y6 == 0.9 and classify == 5:
        return 4,5


    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 0:
        return 5,0
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 1:
        return 5,1
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 2:
        return 5,2
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 3:
        return 5,3
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 4:
        return 5,4
    elif y1 == 0.9 and y2 == 0.9 and y3 == 0.1 and y4 == 0.1 and y5 == 0.1 and y6 == 0.9 and classify == 5:
        return 5,5