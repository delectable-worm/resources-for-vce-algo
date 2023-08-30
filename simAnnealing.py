import random
import copy
import math

#simulated annealing for trying to get the closest subset to goal

def neighbour(A,X):
    Y = copy.deepcopy(X)
    n = len(A)
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    if A[i] in X:
        Y.remove(A[i])
    else:
        Y.append(A[i])
    if A[j] in X and A[j] in Y:
        Y.remove(A[j])
    else:
        Y.append(A[j])
    return Y


def suml(ls):
    sum = 0
    for item in ls:
        sum += item
    return sum

def ranSubset(A):
    output=[]
    for item in A:
        ran = random.randint(0,1)
        if ran == 1:
            output.append(item)
    return output

def annealSum(T,T0,cool,error,d,A): #temp,initial temp, cooling factor, error, goal, superset
    X = ranSubset(A)
    best = X
    while T>T0 and abs(suml(X)-d)>error:
        print("run")
        Y = neighbour(A,X)
        if abs(suml(X)-d) > abs(suml(Y)-d):
            X = Y
            best = Y
            print(best)
        elif random.random() < math.e**(-abs(suml(X)-suml(Y))/T):
            X = Y
        T = T*cool
    return best

print(annealSum(100,10,0.9,1,25,[1,2,3,20,5]))
