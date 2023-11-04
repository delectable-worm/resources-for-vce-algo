import numpy as np
import random
import matplotlib.pyplot as plt

def activation(inputs,weights,bias,w0):
    sum = bias * w0
    for i in range(len(inputs)):
        sum += inputs[i]*weights[i]
    return (1 if sum>0 else 0)

#x1,x2,class
#classifying line x+2
data = [
[1,4,0],
[2,6,0],
[6,10,0],
[3,2,1],
[4,5,1]
]

learn = 0.3

epoch = 1
weights = [3,9]
w0 = 1 # bias weight
bias = 1

for k in range(10):
    for i in range(epoch):
        for j in data:
            inputs = j[0:2]
            exp = j[2]
            predict = activation(inputs,weights,bias,w0)
            error = exp - predict
            print(j,predict)
            if error != 0:
                for i in [0,1]:
                    weights[i] = weights[i] + learn*error*inputs[i]
                w0 = w0 + learn*error*bias
    print("0 = ", weights[0], "x1", weights[1], "x2", w0)
    x = np.linspace(-3,10,100)
    y = -1*(weights[0]*x + w0*bias)/weights[1]

    for d in data:
        if d[2] == 0:
            symbol = "o"
        else:
            symbol = "v"
        plt.plot(d[0],d[1],symbol)
    plt.plot(x,y)
    plt.show()
