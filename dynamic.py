import math
#Some examples for the dynamic programming paradigm. 
#minOp (operator): using a set of operators and operands, find the  minimum number that has to be used to get to a goal.import math


def operator(operator,operand,n):
    dynamic = [0,0]
    for i in range(2,n+1):
        print(i)
        minOperations = math.inf
        for j in range(0,len(operator)):
            if operator[j] == "/":
                if i % operand[j] == 0: #divides
                    minOperations = min(minOperations,dynamic[i//operand[j]]+1)
                    #print(i,operator[j],operand[j], "=",i//operand[j], ": ",minOperations)
            else:
                if i - operand[j] >= 1:
                    minOperations = min(minOperations,dynamic[i-operand[j]]+1)
                    #print(i,operator[j],operand[j], "=",i-operand[j], ": ",dynamic,minOperations)
        print(i,minOperations)
        dynamic.append(minOperations)

    return dynamic

op1 = ["-","/","-"]
op2 = [1,5,3]

print(operator(op1,op2,15))

#a comparison of fibonacci algorithms

    
def dFib(n): #input n>1
    dynamic = [1,1]
    for i in range(2,n):
        dynamic.append(dynamic[i-1]+dynamic[i-2])
    return(dynamic)

print(dFib(6))