# Anagram detection Example

'''def anagramsolution(s1,s2):
    stillok=True
    if len(s1)!=len(s2):
        stillok=False

    alist=list(s2)
    pos1=0

    while pos1<len(s1) and stillok:
        pos2=0
        found=False
        while pos2<len(alist):
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1

        if found:
            alist[pos2]=None
        else:
            stillok=False
        pos1=pos1+1
    return  stillok

print(anagramsolution('abcd','dcba'))'''

'''def anagramSolution1(s1,s2):
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))'''

#Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n2).
# The second function should be linear O(n)
'''
def find_min(astring):
    overall_min=astring[0]
    for i in astring:
        is_smallest=True
        for j in astring:
            if i>j:
                is_smallest=False
        if is_smallest:
            overall_min=i
    return overall_min
print(find_min([9,8,4,6,7,10]))'''

# Second approach
'''
def find_min(list):
    is_smallest=list[0]
    for i in list:
        if is_smallest>i:
            is_smallest=i
    return is_smallest
print(find_min([5,7,4,6,9,10]))'''
