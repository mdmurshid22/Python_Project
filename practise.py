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
Print the final ticket price considering the age, and if applicable, the discounts. '''
username=input("Enter a username:").strip()
password=input("Enter a password:").strip()
if username.lower() == "admin":
	if password.lower() == "password123":
		print("Login successfully")
	else:
		print("Incorrect password")
else:
	print("Invalid username")