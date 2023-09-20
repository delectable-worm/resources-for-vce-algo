import math
import random
def binarySearch(ls, target):
    r = len(ls)-1
    l=0
    mid = (r+l)//2
    while target != ls[mid]:
        mid = (r+l)//2
        if r == l:
            return -1
        elif ls[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return mid, target

#print(binarySearch([0,1,2,3,4,5],4))


def mergeSortr(ls):
    if len(ls) == 1:
        return ls
    else:
        mid = len(ls)//2
        right = mergeSortr(ls[:mid])
        left = mergeSortr(ls[mid:])
        return merge(right,left)
    
def merge(l1,l2):
    k=j=0
    out = []
    while len(l1)>k and len(l2)>j:
        if l1[k] < l2[j]:
            out.append(l1[k])
            k += 1
        else:
            out.append(l2[j])
            j+=1
    if len(l1)<=k:
        for item in l2[j:]:
            out.append(item)
    else:
        for item in l1[k:]:
            out.append(item)
    return out

#print(mergeSortr([1,6,4,2,4,3,9,10]))

def quicksort(ls,lo,hi):
    if lo >= hi or lo < 0:
        return ls
    ls,p = partition(ls,lo,hi)
    print("part",ls,p,lo,hi)
    ls = quicksort(ls,p+1,hi)
    ls = quicksort(ls,lo,p-1)
    return ls

def partition(ls,lo,hi):
    #p = random.randint(lo,hi)
    p = 0
    i = lo
    j = hi
    step = 0
    pv = ls[p]
    print("i,j,p",i,j,p,ls[p])
    while j>i:
        print("i,j,ls,lap",i,j,ls,ls[p])
        if ls[i]<=pv and i<j:
            i += 1
        if ls[j]>=pv and j>i:
            j -= 1
        if ls[i]>pv and ls[j]<pv:
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp
            if ls[i]==pv:
                p = j
            i+=1
            j-=1
    print(i,j)
    
    temp = ls[i]
    ls[i]=pv
    ls[p]=temp
    print(ls)
    return ls, i

#print(quicksort([1,6,4,2,4,3,9,10],0,7))

partition([10,3,6,9,4,1,3],0,6)


