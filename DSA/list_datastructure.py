# Making of list by different way---

# using range function--->

def list1():
    l=[]
    for i in range(1000):
        l=l+[i]

#t1=Timer("test1()","from__main__import test1")
#print("concat",t1.timeit(number=1000),"milliseconds")

def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l=[i for i in range(1000)]

def test4():
    l=list(range(1000))

