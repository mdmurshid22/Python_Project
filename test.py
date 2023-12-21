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
"""a=10
b=20
c=30
print("A:",a)
print("B:",b)
print("C:",c)
print()
a,b,c=b,c,a
print("A:",a)
print("B:",b)
print("C:",c)"""
'''print(dir(str))
s="This Is Python Classroom Classes"
print("Upper Method:",s.upper())
print("Lower Method:",s.lower())
print("Title Method:",s.title())
print("Swapcase Method:",s.swapcase())
print("IsUpper Method:",s.isupper())
print("IsLower Method:",s.islower())
print("IsTitle Method:",s.istitle())
print("StartsWith Method:",s.startswith("t"))
print("EndsWith Method:",s.endswith("s"))
print("Partition Method:",s.partition("c"))
print("RPartition Method:",s.rpartition("c"))
print("Find Method:",s.find("z"))
print("RFind Method:",s.rfind("z"))
print("Index Method:",s.index("P"))
print("RIndex Method:",s.rindex("P"))'''
#Remove spaces with left at first(begining)s.lstrip()
#Remove spaces with right at last(end) s.rstrip()
#Remove spaces with both(begin and end)s.strip()
"""
'capitalize', 
'casefold', 
'center', 
'count', 
'encode', 
'endswith', 
'expandtabs', 
'find', 
'format', 
'format_map', 
'index', 
'isalnum', 
'isalpha', 
'isascii',
'isdecimal', 
'isdigit', 
'isidentifier', 
'islower', 
'isnumeric', 
'isprintable', 
'isspace', 
'istitle', 
'isupper', 
'join', 
'ljust', 
'lower', 
'lstrip', 
'maketrans', 
'partition', 
'removeprefix', 
'removesuffix',  
'replace', 
'rfind', 
'rindex', 
'rjust', 
'rpartition', 
'rsplit', 
'rstrip', 
'split', 
'splitlines', 
'startswith', 
'strip', 
'swapcase', 
'title', 
'translate', 
'upper', 
'zfill'
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
Note: All string methods returns new values. They do not change the original string.
"""