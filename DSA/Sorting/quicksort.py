# python program for implementation of quick sort

# This function takes element as pivot, places 
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all grater elements to right
# of pivot

def partition(arr,low,high):
    i=(low-1)  # index of smaller element
    pivot=arr[high]

    for j in range(low,high):

        # if current element is smaller than the pivot

        if arr[j]<pivot:

            # increment index of smaller element
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)

# The main function that implements Quicksort
# arr[]---> Array to be sorted
# low ---> starting index
# high---> Ending index

# Function to do quick sort
def quicksort(arr,low,high):
    if low<high:

        # pi is partitionong index,arr[p] is now
        # at right place
        pi=partition(arr,low,high)


        # Separtely sort elements before
        # partitionn and after partition
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)


# Code to test
arr=[10,7,8,9,1,5]
n=len(arr)
quicksort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" %arr[i])
    