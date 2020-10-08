'''class dequeue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addfront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removefront(self):
        return self.items.pop()
    def removefrontRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)


d=dequeue()
print(d.isEmpty())
d.addRear(4)
d.addRear("Dog")
d.addRear("Cat")
d.addfront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removefrontRear())
print(d.removefront())
print(d.size())'''

# USE-CASE OF dequeue
from pythonds.basic import Deque
def palchecker(astring):
    chardeque=Deque()
    for ch in astring:
        chardeque.addRear(ch)
    stillequal=True
    while chardeque.size()>1 and stillequal:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillequal=False
    return stillequal

print(palchecker("radar"))
print(palchecker("Yalgar"))
