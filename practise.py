"""number=int(input("Enter Any Number:"))
factorial=number
while number > 1:
	number-=1
	factorial=factorial*number
print("The factorial of given number is:{}".format(factorial))"""
''' Implement a simple login system.
* Ask the user to enter a username and password.
* Check if the entered username is "admin."
* If yes, check if the password is "password123."
* If both conditions are true, print "Login successful."
* If the password is incorrect, print "Incorrect password."
* If the username is incorrect, print "Invalid username."

Ask the user to input three sides of a triangle.
* Check if the triangle is equilateral, isosceles, or scalene.
* Equilateral: All three sides are equal.
* Isosceles: Two sides are equal.
* Scalene: No sides are equal.

Ticket Price Calculator:

Ask the user to input their age.
Determine the ticket price for a movie based on the following conditions:
* If the age is 5 or below, the ticket is free.
* If the age is between 6 and 12 (inclusive), the ticket is $10.
* If the age is between 13 and 17 (inclusive), the ticket is $15.
* If the age is between 18 and 59 (inclusive), the ticket is $20.
* If the age is 60 or above, the ticket is $12.
Additionally, check if the user qualifies for a discount:

* If the user is a student (yes/no), apply a 10% discount to the ticket price.
* If the user is a senior citizen (yes/no), apply a 15% discount to the ticket price.
Print the final ticket price considering the age, and if applicable, the discounts. 
username=input("Enter a username:").strip()
password=input("Enter a password:").strip()
if username.lower() == "admin":
	if password.lower() == "password123":
		print("Login successfully")
	else:
		print("Incorrect password")
else:
	print("Invalid username")
----------------------------------------------------------------------------------------------
side1=float(input("Enter first side of a triangle:"))
side2=float(input("Enter second side of a triangle:"))
side3=float(input("Enter third side of a triangle:"))
if side1 == side2 == side3:
	print("Equilateral:{:.1f} All three sides are equal.".format(side1))
elif side1 == side2:
	print("Isosceles:{} and {} Two sides are equal.".format(side1,side2))
elif side1 == side3:
	print("Isosceles:{1} and {0} Two sides are equal.".format(side3,side1))
elif side2 == side3:
	print("Isosceles:{s3} and {s2} Two sides are equal.".format(s2=side2,s3=side3))
else:
	print("Scalene:%.1f %.1f %.1f No sides are equal." %(side1,side2,side3))
-----------------------------------------------------------------------------------------------
age=int(input("Enter your age above 70 to determine the ticket price for a movie based on the following conditions:"))
student=input("If you are a student(yes/no)?:").strip().lower()
citizen=input("If you are a senior citizen(yes/no)?:").strip().lower()
if student == "yes":
	if (age <= 13) | (age <= 17):
		print("The ticket prize is $5 and age of:{} Discount 10% for student!".format(age))
	elif (age <= 18) | (age <= 59):
		print("The ticket prize is $10 and age of:{} Discount 10% for student!".format(age))
	elif (age <= 60) | (age <= 70):
		print("The ticket prize is $2 and age of:{} Discount 10% for student!".format(age))
	else:
		print("Invalid Input!")
if citizen == "yes":
	if (age <= 5) | ((age <= 6) | (age <= 12)) | ((age <= 13) | (age <= 17)) | ((age <= 60) | (age <= 70)):
		print("Ticket is free and age of:{} Discount 15% for senior citizen!".format(age))
	elif (age <= 18) | (age <= 59):
		print("The ticket prize is $5 and age of:{} Discount 15% for senior citizen!".format(age))
	else:
		print("Invalid Input!")
elif (age <= 5):
	print("Ticket is free and age of:{}".format(age))
elif (age <= 6) | (age <= 12):
	print("The ticket is $10 and age of:{} age".format(age))
elif (age <= 13) | (age <= 17):
	print("The ticket is $15 and age of:{} age".format(age))
elif (age <= 18) | (age <= 59):
	print("The ticket is $20 and age of:{} age".format(age))
elif (age <= 60) | (age <= 70):
	print("The ticket is $12 and age of:{} age".format(age))

1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2500 (both included).
2. Write a Python program that accepts a word from the user and reverses it.
3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
4. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
5. Write a Python program to check whether an alphabet is a vowel.
6. Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 

7. Write a Python program to create the multiplication table (from 1 to 10) of a number.

8. Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999'''
#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
#between 1500 and 2500 (both included).
"""while True:
	number=int(input("Enter Any Number between 1500 to 2500:"))
	if number >= 1500:
		if number <= 2500:
			if number%7 == 0:
				if number%5 == 0:
					print("This {} is Divisible by 7".format(number),end=" ")
					print("and Multiples of five is:{}".format(number))
					break
			else:
				print("This {} is Not Divisible by 7".format(number))
				break
for i in range(1500,2501):
	if i%7 == 0:
		if i%5 == 0:
			print("This {} is Divisible by 7".format(i),end=" ")
			print("and Multiples of five is:{}".format(i))
	else:
		print("This {} is Not Divisible by 7".format(i))
-----------------------------------------------------------------------------------------------------------------
#2. Write a Python program that accepts a word from the user and reverses it.
#Slice operators:-
user_name=input("Enter Your Name:")
print("username is:{} and reverse a username by using slice operators:{}".format(user_name,user_name[::-1]))
#reversed Method:-
user_name=input("Enter Your Name:")
for x in reversed(user_name):
	print(x,end="")
#Python by using while_loop code:-
user_name=input("Enter Your Name:")
i=-1
l=[]
while i >= -len(user_name):
	l.append(user_name[i])
	i-=1
for x in l:
	print(x,end="")
------------------------------------------------------------------------------------------------------------------
#3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for x in range(7):
	if x == 3:
		continue
	elif x == 6:
		continue
	else:
		print(x)
-------------------------------------------------------------------------------------------------------------------
#4. Write a Python program that iterates the integers from 1 to 50. 
#For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
#For numbers that are multiples of three and five, print "FizzBuzz".
num=int(input("Enter Any Number:"))
for i in range(num+1):
	if (i%3 == 0) & (i%5 == 0):
		print(i,"FizzBuzz")
	elif i%3 == 0:
		print(i,"Fizz")
	elif i%5 == 0:
		print(i,"Bizz")
-------------------------------------------------------------------------------------------------------------------
#5. Write a Python program to check whether an alphabet is a vowel.
#input:ababababab
#output:a=5
char=input("Enter Any substring:")
vowels='aeiouAEIOU'
i=0
l=[]
while i < len(vowels):
	for x in char:
		if vowels[i] == x:
			l.append(x) 
	i+=1
for j in l:
	print(j,end="")
---------------------------------------------------------------------------------------------------------------------------
6. Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January:31, February:29, March:31, April:30, May:31, June:30, July:31, August:31,
September:30, October:31, November:30, December:31.                                
Input the name of Month: February                                       
No. of days: 28/29 days
month=input("Enter Any Month:").strip().capitalize()
if ('January' == month) | ('March' == month) | ('May' == month) | ('July' == month) | ('August' == month) | ('October' == month) | ('December' == month):
	print("No. of days: 31 days in {}.".format(month))
elif 'February' == month:
	print("No. of days: 29 days in {}.".format(month))
elif ('April' == month) | ('June' == month) | ('September' == month) | ('November' == month):
	print("No. of days: 30 days in {}.".format(month))
else:
	print("Invalid Input:{}".format(month))
-----------------------------------------------------------------------------------------------------------------------------
#7. Write a Python program to create the multiplication table (from 1 to 10) of a number.
num=int(input("Enter any table number:"))
print("{} Table:-".format(num))
for x in range(1,10+1):
	print("{} * {} = {}".format(x,num,num*x))
-----------------------------------------------------------------------------------------------------------------------------
8. Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
num=int(input("Enter Any Number of Rows:"))
for x in range(1,num+1):
	print(str(x)*x)
--------------------------------------------------------------------------------------------------------------------------------
#1. Sum of first N Numbers by using while_loop?
#input:7
#output:1+2+3+4+5+6+7+8:36
num=int(input("Enter sum of numbers:"))
i=1
output=0
while i <= num:
	output=output+i
	i+=1
print(output)
#Sum of first N Numbers by using for_loop?
num=int(input("Enter sum of number:"))
result=0
for x in range(1,num+1):
	result=result+x
print(result)
----------------------------------------------------------------------------------------------------------------------------
#2. output:1*10
           2*9
           3*8
           4*7
		   5*6
i=int(input("Enter First Number:"))
j=int(input("Enter Second Number:"))
while i <= j:
	print(i,j)
	i+=1
	j-=1
-----------------------------------------------------------------------------------------------------------------------------
#3. output:1 2 4 7 11 16 22 29 37
number=int(input("Enter Any Number:"))
initial_number=1
multiply_number=0
while multiply_number <= number:
	initial_number=initial_number+multiply_number
	multiply_number+=1
	print(initial_number,end=" ")
----------------------------------------------------------------------------------------------------------------------------
#4. Write a Python program to given number is Prime or not:-
#2, 3, 5, 7, 11, 13, 17, 19, 23 . . .
num=int(input("Enter Any Number is prime or not:"))
prime=True
i=2
while i < num:
	if num%i == 0:
		print("Not Prime, It's Composite Number.")
		prime=False
		break
	i+=1
if (num == 0) | (num == 1):
	print("Neither a Prime Number nor a Composite Number, It's Unique Number.")
elif prime == True:
	print("Prime Number")
#5. Fibonacci series:-
#0, 1, 1, 2, 3, 5, 8, 13 ...
num=int(input("Enter Any Number:"))
i=0
j=1
for x in range(num):
	print(i,end=" ")
	if i == 13:
		break
	k=i+j
	i=j
	j=k
----------------------------------------------------------------------------------------------------------------------------
#6. LCM(Least Common Multiple):-
#Example 2,: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 ...
#Example 6,: 6, 12, 18, 24, 30, 36 ...
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
if n1 > n2:
	max=n1
else:
	max=n2
while True:
	if (max%n1 == 0) & (max%n2 == 0):
		lcm=max
		break
	max+=1
print("LCM:{}".format(lcm))
-------------------------------------------------------------------------------------------------------------------------------
#7. GCD(Greatest Common Divisor), HCF(Heighest Common Factor)
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
if n1 < n2:
	min=n1
else:
	min=n2
while min >= 2:
	if (n1%min == 0) & (n2%min == 0):
		print("GCD:{}".format(min))
		break
	min-=1
---------------------------------------------------------------------------------------------------------------------------------
#8. Find the Square root of given number:-
root=int(input("Enter Any Number:"))
i=2
while(i <= root/2):
	if(root/i == i):
		print("Square Root of a Number is:{}".format(i))
		break
	i+=1
----------------------------------------------------------------------------------------------------------------------------------
#9. Find the Factorial of given number:-
num=int(input("Enter Any Number:"))
fact=num
while num > 1:
	num-=1
	fact=fact*num
print("Factorial of given number is:{}".format(fact))"""
#10. Reverse a Number and palindrome program:-
num=int(input("Enter Any Number:"))
print("Actual Number:{}".format(num))
rem=0
while num > 0:
	rem=(rem*10)+num%10
	num=num//10
print("Reverse a Number:{}".format(rem))