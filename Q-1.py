class ComplexNumber:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,num1,num2):
        print("Addition result :",(num1+num2))

    def mul(self,num1,num2):
        print("Multiplication result :",(num1*num2))
        
    def sub(self,num1,num2):
        print("Subtraction result :",(num1-num2))

    def div(self,num1,num2):
        print("Division result :",(num1/num2))

num1 = complex(input("Enter 1st complex number :"))   
num2 = complex(input("Enter 2nd complex number :"))
print("Arithmetic operations are :")

cmplx = ComplexNumber(num1,num2)
cmplx.add(num1,num2)
cmplx.sub(num1,num2)
cmplx.mul(num1,num2)
cmplx.div(num1,num2)

#OUTPUT:
# Enter 1st complex number :3+7j
# Enter 2nd complex number :0-9j
# Arithmetic operations are :
# Addition result : (3-2j)
# Subtraction result : (3+16j)
# Multiplication result : (63-27j)
# Division result : (-0.7777777777777778+0.3333333333333333j)
