# CALCULATOR : 

num1 = int(input("enter a digit : "))
num2 = int(input("enter another digit : "))
choose = input("choose an option(a,b,c or d) for calculation :\n(a) add\n(b) sub\n(c) multiply\n(d) div : ")

class calculator:
    def __init__(self,a,b):
        self.number1=a
        self.number2=b
    def add(self):
        result=self.number1+self.number2
        return print(f"The sum of the {self.number1} and {self.number2} is {result}")
    def sub(self):
        result=self.number1-self.number2
        return print(f"The difference of {self.number1} and {self.number2} is {result}")
    def multiply(self):
        result=self.number1*self.number2
        return print(f"The product of {self.number1} and {self.number2} is {result}")
    def div(self):
        if self.number2==0:
            return print(" THIS NUMBER IS NOT DIVIDIBLE BY ZERO ")
        else:
            result=self.number1/self.number2
            return print(f"the quotient of {self.number1} and {self.number2} is {result}")

#object calling:
obj=calculator(num1,num2)

if choose=="a":
    obj.add()
elif choose=="b":
    obj.sub()
elif choose=="c":
    obj.multiply()
elif choose=="d":
    obj.div()
else:
    print("Invalid option choose the option correctly....")