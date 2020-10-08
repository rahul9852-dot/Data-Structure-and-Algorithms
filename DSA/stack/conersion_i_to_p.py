# Python program to convert infix expression to postfix

# Classs to convert the expression
class conversion:

    # Constructor to iitialize the class variable

    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        # This array used as stack
        self.array=[]
        # Precedence setting
        self.output=[]
        self.Precedence={"'+":1,"-":1,"*":2,'/':2,"^":3}

     #check if the stack is empty
    def isempty(self):
        return True if self.top==-1 else False
        
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from stack
    def pop(self):
        if not self.isempty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack

    def push(self,op):
        self.top+=1
        self.array.append(op)

    # A utility function to check is the given
    # charcter is operand

    def isoperand(self,ch):
        return ch.isalpha()
        
    # Check if the precedence of operator is strictly
    # less than top of stack or not

    def notgreater(self,i):
        try:
            a=self.Precedence[i]
            b=self.Precedence[self.peek()]
            return True if a <=b else False
        except KeyError:
            return False
    
    # The main function that converts given infix expression
    # to postfix expression

    def infixtopostfix(self,exp):

        # Itearte over the expression for conversion
        for i in exp:
            # If the charcter is an operand
            # add it to output
            if self.isoperand(i):
                self.output.append(i)

            # If the charcter is an '(', push it on 
            # stack

            elif i=="(":
                self.push(i)

            # If the scanned charcter is an ")" , pop
            # and output from the stack until and "(" is found

            elif i==")":
                while ((not self.isempty()) and self.peek()!='('):
                    a=self.pop()
                    self.output.append(a)

                if (not self.isempty() and self.peek()!="("):
                    return -1
                else:
                    self.pop()


            # An operator is encountered 
            else:
                while (not self.isempty() and self.notgreater(i)):
                    self.output.append(self.pop())

                self.push(i)

        # Pop all the operator from stack
        while not self.isempty():
            self.output.append(self.pop())
        print("".join(self.output))


# test above function

exp="a+b*(c^d-e)^(f+g*h)-i" 
obj=conversion(len(exp))
obj.infixtopostfix(exp)


        