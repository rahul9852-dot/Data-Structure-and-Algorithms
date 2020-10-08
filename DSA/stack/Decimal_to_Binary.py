from pythonds import Stack
def divideby2(decnumber):
    remstack=Stack()
    while decnumber>0:
        rem=decnumber%2
        remstack.push(rem)
        decnumber=decnumber//2
    binstring=""
    while not remstack.isEmpty():
        binstring=binstring+str(remstack.pop())

    return binstring
print(divideby2(42))

'''def baseconverter(decnumber,base):
    digits="0123456789ABCDEF"

    remstack=Stack()

    while decnumber>0:
        rem=decnumber%base
        remstack.push(rem)
        decnumber=decnumber//base

    newstring=""
    while not remstack.isEmpty():
        newstring=newstring+digits[remstack.pop()]
    return newstring

print(baseconverter(25,2))
print(baseconverter(256,16))'''
