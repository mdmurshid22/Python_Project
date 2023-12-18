'''n=int(input("Enter Some Number:"))
for i in range(n):
	print("* "*n)
-----------------------------------------	
n=int(input("Enter Some Number:"))
for i in range(n):
	print("* "*(i+1))
-----------------------------------------
n=int(input("Enter Some Number:"))
for i in range(1,n+1):
	print("* "*i);
for i in range(1,n+1):
	print("* "*(n-i))'''
n=int(input("Enter Some Number:"))
for i in range(1,n+1):
	print((" "*(n-i))+(" *"*i))