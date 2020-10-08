'''

Q.1 for i in range(n):
        for j in range(n):
                k=k+2
                O(n^2)
Q.2 for i in range(n):
        k=k+2
        O(n)
Q.3 i=n
        while i>0:
            k=k+2
            i=i//2
            O(logn)
Q.4  for i in range(n):
            for j in range(n):
                for k in range(n):
                    k=k+2
                    O(n^3)
Q.5  for i in range(n):
        k=k+2
        for j in range(n):
            k=k+2
        for k in range(n):
            k=2+2
            O(n^3)
'''

# Programmin Exercise

'''import timeit
import random

for i in range(10000, 1000000, 20000):
    t = timeit.Timer("x.index(random.randrange(%d))"%i,
                     "from __main__ import random, x")


    x = list(range(i))
    indextime = t.timeit(number=100)
    print("%d, %10.4f" %(i, indextime))'''

# Discussion Question on Linear Data Structure
#Q.1 convert decimal to binary
'''from pythonds.basic import Stack
def dividedby2(dec_num):
    remstack=Stack()
    while dec_num>0:
        rem=dec_num%2
        remstack.push(rem)
        dec_num=dec_num//2
    binstring=""
    while not remstack.isEmpty():
        binstring=binstring+str(remstack.pop())
    return binstring

print(dividedby2(17))
print(dividedby2(45))
print(dividedby2(96))'''
