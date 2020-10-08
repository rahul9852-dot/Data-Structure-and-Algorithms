# Recursion
'''def list_sum(num_list):
    if len(num_list)==1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
print(list_sum([1,3,5,7,9]))'''

# Factorial

'''def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))'''

def to_str(n,base):
    convertstring="0123456789ABCDEF"
    if n<base:
        return convertstring[n]
    else:
        return to_str(n//base,base)+convertstring[n%base]

print(to_str(1453,16))

# Stack Frames: Implementing Recursion
'''from pythonds import Stack
def to_str(num,base):
    rstack=Stack()
    convert_string="0123456789ABCDEF"
    while num>0:
        if num<base:
            rstack.push(convert_string[num])
        else:
            rstack.push(convert_string[num%base])
        num=num//base
    res=""
    while not rstack.isEmpty():
        res=res+str(rstack.pop())
    return res
print(to_str(1453,16))'''


# Visualizing Recursion

'''import turtle
my_turtle=turtle.Turtle()
mywin=turtle.Screen()
def drawspiral(my_turtle,linelen):
    if linelen>0:
        my_turtle.forward(linelen)
        my_turtle.right(90)
        drawspiral(my_turtle,linelen-5)
drawspiral(my_turtle,100)
mywin.exitonclick()
'''
'''
import turtle
def tree(branchlen,t):
    if branchlen>5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(branchlen-15,t)
        t.right(20)
        t.backward(branchlen)
def main():
    t=turtle.Turtle()
    mywin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    mywin.exitonclick()
main()'''

import turtle
'''
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)'''
'''
def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()'''