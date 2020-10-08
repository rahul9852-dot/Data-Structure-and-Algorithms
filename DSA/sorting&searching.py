# Sequential searching
'''
def sequential_serach(a_list,item):
    pos=0
    found=False
    while pos<len(a_list) and not found:
        if a_list[pos]==item:
            found=True
        else:
            pos+=1
    return found

test_list=[1,2,32,8,17,19,42,13,0]

print(sequential_serach(test_list,3))
print(sequential_serach(test_list,13))'''
'''
def sequential_search(a_list,item):
    pos=0
    found=False
    stop=False
    while pos<len(a_list) and not found and not stop:
        if a_list[pos]==item:
            found=True
        else:
            if a_list[pos]>item:
                stop=True
            else:
                pos+=1
    return found

test_case=[0,1,2,8,13,17,19,32,42]

print(sequential_search(test_case,3))
print(sequential_search(test_case,13))'''


# Binary_search

def binary_serach(a_list,item):
    first=0
    found=False
    last=len(a_list)-1
    while first<last and not found:
        mid_point=first+last//2
        if a_list[mid_point]==item:
            found=True
        else:
            if item<a_list[mid_point]:
                last=mid_point-1
            else:
                first=mid_point+1
    return found

test_case=[0,1,2,8,13,17,19,32,42]

print(binary_serach(test_case,3))
print(binary_serach(test_case,13))