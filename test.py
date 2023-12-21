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
'''input1=eval(input("Arithmetic Operators Values:"))
input2=eval(input("Arithmetic Operators Values:"))
print("Addition:",input1+input2)
print("Subtraction:",input1-input2)
print("Multiplication:",input1*input2)
print("Division:",input1/input2)
print("Modulus:",input1%input2)
print("Floor Division:",input1//input2)
print("Exponentiation:",input1**input2)'''
'''day=input("Enter First Number:")
month=input("Enter First Number:")
year=input("Enter First Number:")
print(day,month,year,sep="/")
print(day,month,year,sep="-")'''
#import keyword
#print(len(keyword.kwlist))
#print(ord('A'))
#print(chr(87))
#s="This is Python"
#print(s[8:14])
'''print(s)
print(id(s))
print()
s1=s.replace("Python","Java")
print(s1)
print(id(s1))'''
"""a="This is a Python Class"
b="Java and HTML"
print(a[:9],b[9:])
print(a[:9],b[0:4],a[10:16])"""
"""num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
print("Two Numbers is Equal" if num1 == num2 else "Number 1 is Bigger" if num1 > num2 else "Number 2 is Greater")"""
#a='56789'
#print(a[-3::-1]+a[3:])
#print(len(dir(str())))
a=10
b=20
c=30
print("A:",a)
print("B:",b)
print("C:",c)
print()
a,b,c=b,c,a
print("A:",a)
print("B:",b)
print("C:",c)