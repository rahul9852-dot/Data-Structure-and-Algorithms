# Python program to find an element x 
# in a sorted array using Exponential Search 
  
# A recurssive binary search function returns  
# location  of x in given array arr[l..r] is  
# present, otherwise -1

def binary_search(arr,l,r,x):
    if r>=1:
        mid=l+(r-1)//2

        # if the element present at
        # middle itself 
        if arr[mid]==x:
            return mid
        # If the element is smaller than mid,  
        # then it can only be present in the  
        # left subarray
        if arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        # Else he element can only be 
        # present in the right 

        return binary_search(arr,mid+1,r,x)

    # We reach here if the element is not present
    return -1

# Returns the position of first 
# occurrence of x in array 
def exponentialsearch(arr,n,x):
    # IF x is present at first  
    # location itself
    if arr[0]==x:
        return 0
    # Find range for binary search  
    # j by repeated doubling 
    i=1
    while i<n and arr[i]<=x:
        i=i*2

    # Call binary search for the found range
    return binary_search(arr,i/2,min(i,n),x)

arr=[2,3,4,10,40]

n=len(arr)
x=10
result=exponentialsearch(arr,n,x)
if result==-1:
    print("Element not found in the array")
else:
    print("Element is present at index %d" %(result))




