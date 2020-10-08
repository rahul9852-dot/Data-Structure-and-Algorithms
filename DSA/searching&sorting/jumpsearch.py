# Jump search
#Jump Search is a searching algorithm for sorted arrays. 
# The basic idea is to check fewer elements 
# (than linear search) by jumping ahead by fixed steps or 
# skipping some elements in place of searching all elements.

import math

def jumpsearch(arr,x,n):

    # finding block size to be jumped
    step=math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev=0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1

    # Doing a linear search for x in
    # Block begining with prev
    while arr[int(prev)]<x:
        prev+=1


        # if we reached next block or end
        # of array, element is not present
        if prev==min(step,n):
            return -1

    # If element is found
    if arr[int(prev)]==x:
        return prev
    return -1

arr=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
x=55
n=len(arr)

# find the index of 'x' using Jump Search
index=jumpsearch(arr,x,n)

# print the index where 'x' is located
print("Number" ,x, "is at index","%.0f"%index)

    