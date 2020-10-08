import time
from random import randrange
'''def sumofn(n):
    start=time.time

    thesum=0
    for i in range(1,n+1):
        thesum+=i
    end=time.time()

    return thesum,end-start

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumofn(1000))'''

'''import time

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000))'''

'''def sumofN3(n):
    return(n*(n+1))//2

print(sumofN3(10))'''

# for n-square
'''def findmin(list):
    overallmin=list[0]
    for i in list:
        issmallest=True
        for j in list:
            if i>j:
                issmallest=False
        if issmallest:
            overallmin=i
    return overallmin'''


'''def findmin(alist):
    minsofar=alist[0]
    for i in alist:
        if i<minsofar:
            minsofar=i
    return minsofar


print(findmin([5,4,2,1,0]))'''
#print(findmin([0,4,2,1,5]))

'''for listsize in range(1000,10001,1000):
    alist=[randrange(100000)for x in range(listsize)]
    start=time.time()
    print(findmin(alist))
    end=time.time()
    print("size: %d time: %f"%(listsize,end-start))
'''

'''for listsize in range(1000,10001,1000):
    alist=[randrange(100000)for x in range(listsize)]
    start=time.time()
    print(findmin(alist))
    end=time.time()
    print("size: %d time: %f" %(listsize,end-start))'''


'''list=[14,12,3,2,6,9]
for i in range (0,len(list)):
    for j in range(i,len(list)):
        if list[j]>list[j+1]:
            list[j]=list[j+1]
        else:
            list[j]
        j=j+1
        print(j)'''

'''def find_min(list):
     is_small=list[0]
     for i in list:
        if i<is_small:
            is_small=i
     return is_small
print(find_min([5,9,7,4,10,12]))'''
from timeit import Timer
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
popzero.timeit(number=1000)
#4.8213560581207275

x = list(range(2000000))
popend.timeit(number=1000)
#0.0003161430358886719
