'''num1=input("Enter First Number?")
num2=input("Enter Second Number?")
print("Num1:",num1)
print("Num2:",num2)
temp = num1
num1 = num2
num2 = temp
print("Num1:",num1)
print("Num2:",num2)
--------------------------------------------
num1=input("Enter First Number:")
num2=input("Enter Second Number:")
print("Num1:",num1)
print("Num2:",num2)
num1,num2=num2,num1
print("Num1:",num1)
print("Num2:",num2)'''
#print("Idiot"+" "+input("Enter Your Name:"))
#print(input("Enter Your Name:")+" "+"idiot")
#Biswise operators:-(&,|,^)
"""a=25
b=15
print(a & b)
print(a | b)
print(a ^ b)
print(bin(5))
print(bin(10))
print("& operator:",0b1000)
print("| operator:",0B1000)
print("^ operator:",0b0000)"""
#print(bool(input("Enter Boolean Values:")))
#print(float(input("Enter Floting-Point Values:")))
#print(int(input("Enter Integral Values:")))
#print(eval(input("Enter Any Values:")))
#print(input("Enter String Values:"))
#Arithmetic operators:-(+,-,*,/,%,//,**)
input1=eval(input("Arithmetic Operators Values:"))
input2=eval(input("Arithmetic Operators Values:"))
print("Addition:",input1+input2)
print("Substration:",input1-input2)
print("Multiplication:",input1*input2)
print("Division:",input1/input2)
print("Madulo Divition:",input1%input2)
print("Floor Divition:",input1//input2)
print("Power Operator:",input1**input2)