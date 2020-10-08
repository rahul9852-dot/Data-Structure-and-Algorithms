 from pythonds import Stack
'''def parchecker(symbolstring):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolstring) and balanced:
        symbol=symbolstring[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open,close):
    opens="([{"
    closers=")]}"
    return opens.index(open)==closers.index(close)
#print(parchecker('((()))'))
#print(parchecker('(()'))

print(parchecker('{({([][])}())}'))
print(parchecker('[{()]'))'''

'''def par_check(astring):
    s=Stack()
    balanced=True
    index=0
    while index<len(astring) and balanced:
        symbol=astring[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(par_check('((()))'))
print(par_check('(()'))'''

def par_check(astring):
    s=Stack()
    balanced=True
    index=0
    while index<len(astring) and balanced:
        symbol=astring[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
            index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens="([{"
    closers=")]}"
    return open.index(open)==closers.index(close)

print(par_check('{({([][])}())}'))
print(par_check('[{()]'))
