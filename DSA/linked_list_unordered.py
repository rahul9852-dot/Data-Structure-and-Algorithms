# Listing 1
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,newdata):
        self.data=newdata
    def setnext(self,newnext):
        self.next=newnext
    def showdata(self):
        print("The data in list is",self.data)


# Listing 2
class unorderedlist:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setnext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getnext()
        return count
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getdata()==item:
                found=True
            else:
                current=current.getnext()
        return found
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getnext()
        if previous==None:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())
mylist=unorderedlist()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
