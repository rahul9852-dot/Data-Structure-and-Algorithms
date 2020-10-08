# Linear_search 

def linear_search(alist,item):
    pos=0
    found=False

    while pos<len(alist) and not found:
        if alist[pos]==item:
            return True
        else:
            pos+=1
    return found

testlist=[1,2,32,8,17,19,42,13,0]
print(linear_search(testlist,3))
print(linear_search(testlist,13))

# complexity of linear serach is more because 
# comparing each and every item as we know that number 
# of comparsion cost more.

# Slightly, we can reduce our complexity when 
# we have sorted list. we don't check the element who 
# is greater than item we are seraching for.

def linear_search1(alist,item):
    pos=0
    found=False
    stop=False
    while pos < len(alist) and not found and not stop:
        if alist[pos]==item:
            return True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    return found

alist=[1,2,3,4,5,6,7,8,9,10]
print(linear_search1(alist,3))
print(linear_search1(alist,13))
