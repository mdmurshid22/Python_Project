'''1. Write a Python program to find common items from two lists

Sample Output

[23,45,67,78,89,34]

[34,89,55,56,39,67]

Common items from two lists : {89, 34, 67}

2. Create a list by concatenating a given list which range goes from 1 to n

Sample Output

['T', 'J']

N = 10

['T1', 'J1', 'T2', 'J2', 'T3', 'J3', 'T4', 'J4', 'T5', 'J5', 'T6', 'J6', 'T7', 'J7', 'T8', 'J8', 'T9', 'J9', 'T10', 'J10']

3. Write a Python program to convert a list of characters into a string

Sample Output

['p','y','t','h','o','n']

python

4. Write a Python program to select the odd number of a list

Sample Output

[1,2,4,3,6,7,5,8,9,7,8,9,10]

5. Write a Python Program to count unique values inside a list

Sample Output

[10, 20, 30, 50, 80, 70, 70, 80, 10]

No of Unique Items in List : 6

6. Write a Python program to find the repeated items of a tuple

Sample Output

(2, 34, 45, 6, 7, 2, 4, 5, 78, 34, 2)

item = 2

Repeated items of a tuple = 3


7. Write a Python program to convert a tuple to a dictionary

Sample Output

( ("Name", "Ram"), ("Age", 23), ("City", "Salem"), ("Mark", 422) )

{ 'Name': 'Ram', 'Age': 23, 'City': 'Salem', 'Mark': 422 }

8. Write a Python program to find maximum and the minimum value in a set

Sample Output

{17, 56, 23, 8, 10, 45}

Maximum : 56

Minimum : 8

9. Write a Python program to iterate over dictionaries using for loops.

Sample Output

{"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

Name : Ram

Age : 23

City : Salem

Gender : Male

10. Write a program to sum all the values of a dictionary.

Sample Output

Dictionary = { "m1" : 92 , "m2" : 56 , "m3" : 88 , "m4" : 97 , "m5" : 89 }

Sum of Values = 422
-------------------------------------------------------------------------------------------------------------------------
1. Write a Python program to find common items from two lists

Sample Output

[23,45,67,78,89,34]

[34,89,55,56,39,67]

Common items from two lists : {89, 34, 67}
l1=[23,45,67,78,89,34]
l2=[34,89,55,56,39,67]
l3=[]
l4=[]
index=0
while index <= len(l1)-1:
	if l1[index] in l2:
		l3.append(l1[index])
	else:
		l4.append(l1[index])
	index+=1
print('l1:{}'.format(l1))
print('l2:{}'.format(l2))
print('Comman values is:{}'.format(l3))
print('Non comman values is:{}'.format(l4))
---------------------------------------------------------------------------------------------------------------------------
2. Create a list by concatenating a given list which range goes from 1 to n

Sample Output

['T', 'J']

N = 10

['T1', 'J1', 'T2', 'J2', 'T3', 'J3', 'T4', 'J4', 'T5', 'J5', 'T6', 'J6', 'T7', 'J7', 'T8', 'J8', 'T9', 'J9', 'T10', 'J10']
----------------------------------------------------------------------------------------------------------------------------
num=int(input("Enter Some Number:"))
l=eval(input("Enter Some List:"))
index=0
l1=[]
while index <= len(l)-1:
	for x in range(1,num+1):
		l1.append(l[index]+str(x))
	index+=1
print(l1)
---------------------------------------------------------------------------------------------------------------------------
3. Write a Python program to convert a list of characters into a string

Sample Output

['p','y','t','h','o','n']

python
li=eval(input('Enter Any List of Characters:'))
output=''
index=0
while index <= len(li)-1:
	print(li[index],end="")
	index+=1
---------------------------------------------------------------------------------------------------------------------------'''