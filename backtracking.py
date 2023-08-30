import copy as cp

#backtracking design pattern demo for filling a latin square. No repeats in rows or columns for 1 to n on n^2 board.

def latinsquare(m,i=0,j=0,output=[]): #"-" indicates null value
    if correct(m):
        m = cp.deepcopy(m) #needed because python memory just stores pointers
        output.append(m)
        return output
    else:
        tentative = cp.deepcopy(m)
        print(i,j)

        if j < len(m)-1: #move right
            j += 1
        elif j==len(m)-1 and i==(len(m))-1: #finished array
            return output
        else: #move to new row
            i+=1
            j=0

        while m[i][j]!="-": #same as above: keep moving across filled tiles
            print(i,j)
            if j < len(m)-1:
                j += 1
            elif j==len(m)-1 and i==(len(m))-1:
                return output
            else:
                i+=1
                j=0

        for k in range(1,len(m)+1): #try all numerical values
            tentative[i][j] = k
            if check(tentative,j,i):
                call = latinsquare(tentative,i,j,output) #recur for new board
                if not call == None: #can't call return here as it breaks out of this loop and halts! Output equals none if no correct children in call tree; otherwise, correct output is appended as in base case.
                    output = call
    return output
    
for k in range(1,3+1):
    print(k)

def correct(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if not check(m,i,j) or m[i][j] == "-": return False

    return True

def check(m,x,y):
    appeared = {}
    for j in m[y]: #row
        if j in appeared and not j == "-":
            return False
        appeared[j] = 1
    appeared.clear()
    for j in range(len(m)):
        i = m[j][x]
        if i in appeared and not i == "-":
            return False
        appeared[i] = 1
    return True


print("putput:",latinsquare([[1,2,3],["-","-","-"],["-","-","-"]]))



#Sum to k backtracking

import copy
def sumto(goal,superset,subset=[],i=0,output=[]):
    if sum(subset) == goal:
        output.append(subset)
        return output
    elif sum(subset) > goal or i == len(superset)-1:
        return output
    else:
        s1 = copy.deepcopy(subset)
        s2 = copy.deepcopy(subset)
        output=sumto(goal,superset,s1,i+1,output)
        s2.append(superset[i])
        output=sumto(goal,superset,s2,i+1,output) #valid combinations appened to output always
        return output

        
def sum(ls):
    s = 0
    for item in ls:
        s = s + item
    return s

print(sumto(10,[2,3,4,5,6,7,8]))