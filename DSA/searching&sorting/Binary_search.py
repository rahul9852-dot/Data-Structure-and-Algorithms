# Binary search algorithms for serrching element into the list

def binary_search(alist,item):
    low=0
    high=len(alist)-1
    found=False
    while low<high and not found:
        mid_term=(low+high)//2 
        # check x is present at mid
        if alist[mid_term]==item:
            print("Found at index",mid_term)
            return True
        # item is smaller ,ignore right half
        else:
            if item<alist[mid_term]:
                high=mid_term-1
        # item is greater,ignore left half
            else:
                low=mid_term+1
    # else we reach here element are not present
    return found

alist=[2,5,8,12,16,23,38,56,72,91]
print(binary_search(alist,23))

# Recursive Implementation of Binary search

def binary_search1(arr,l,r,x):

    # Check base case
    if r>=l:

        mid=(l+r)//2

        #if element found at middle itself
        if arr[mid]==x:
            return mid

        #If element is smaller than mid, then it
        # can only present in left subarray

        elif arr[mid]>x:
            return binary_search1(arr,l,mid-1,x)
        
        #else the element can only be present 
        # in right subarray
        else:
            return binary_search1(arr,mid+1,r,x)

    else:
        return -1

arr=[2,3,4,10,40]
x=10

#Function call
result=binary_search1(arr,0,len(arr)-1,x)

if result!=-1:
    print("Element is present at index %d"% result)
else:
    print("Element is not present in array")