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
	print("The ticket is $12 and age of:{} age".format(age)) '''