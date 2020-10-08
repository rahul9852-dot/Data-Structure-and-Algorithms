# Python program for implementation of bubble sort

def bubble_sort(alist):
    n=len(alist)
    # Traverse through all array in place
    for i in range(n):

        # Last element already in place
        for j in range(0,n-i-1):

            # traverse the array from 0 to n-1
            # Swap if the element found is greater
            # than the next element
            if alist[j]>alist[j+1]:
 
                   alist[j],alist[j+1]=alist[j+1],alist[j]

# for test the code
alist=[64,34,25,12,22,11,90]
bubble_sort(alist)
print("Sorted alist is:")
for i in range(len(alist)):
    print("%d"%alist[i])

