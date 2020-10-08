# Python Program for implementation of selection
#sort

a=[64,25,12,22,11]

# Traverse through all array elements.
for i in range(len(a)):

    # Find the minimun element in remaining
    # unsorted array

    min_idx=i
    for j in range(i+1,len(a)):
        if a[min_idx]>a[j]:
            min_idx=j
    a[i],a[min_idx]=a[min_idx],a[i]

# test code
print("Sorted array")
for i in range(len(a)):
    print("%d" %a[i])