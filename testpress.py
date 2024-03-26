'''#TestPress.

1. Write a program to print the reverse of the given string.
Input
codecode
Output
edocedoc
Input Constraints
1<=Length of string<=100
Input string contains only lowercase characters ['a' to 'z'].

https://onlinegdb.com/oM20oPpNS

#1)Using Slice operator.

lower_case_char = input("Enter Any Lower Case Characters:")
print(lower_case_char[::-1])

#2)Using Reversed and Join Methods.

lower_case_char = input("Enter Any Lower Case Characters:")
print(''.join(reversed(lower_case_char)))

#3)Using Python Code.

lower_case_char = input("Enter Any Lower Case Characters:")
index = -1
Character_list = []
Character_length = -len(lower_case_char)
while index >= Character_length:
	Character_list.append(lower_case_char[index])
	index -= 1
for x in Character_list:
	print(x,end="")
--------------------------------------------------------------------------------------------------------------------------------------------------------
2. Given a number, check whether it is a prime number or not.
Input 1
3
Output 1
Yes
Input 2
4
Output 2
No

https://onlinegdb.com/A7R1v6uUJ

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
------------------------------------------------------------------------------------------------------------------------------------------------------
3. Given an array of numbers, arrange them in a way that it forms the largest value.
Input
[54, 546, 548, 60]
Output
6054854654

https://onlinegdb.com/VGciMrDPV

list_arrary = eval(input("Enter Any Array of List:"))
length_list = -len(list_arrary)
empty_list = []
index = -1
while index >= length_list:
	empty_list.append(list_arrary[index])
	index -= 1
for x in empty_list:
	print(int(x),end='')
------------------------------------------------------------------------------------------------------------------------------------------------------
4. Given a number N, print reverse of number N.
Input
988
Output
889
Note
Do not print leading zeros in output.
For example N = 100
Reverse of N should be 1 not 001.
Constraints
1<=N<=10000

https://onlinegdb.com/M0ldlUIcJ

Number = int(input("Enter Any Numbers and Reversed that Numbers:"))
Num = ''.join(reversed(str(Number)))
print(int(Num))
------------------------------------------------------------------------------------------------------------------------------------------------------
5. Given an array of numbers, find the maximum and minimum element in the array.
Input
[54, 546, 548, 60]
Output
548 54

https://onlinegdb.com/zyHMartWn

list_arrary = eval(input("Enter Any Array of List:"))
print('Maximum Number of given array is:{}'.format(max(list_arrary)))
print('Minimum Number of given array is:{}'.format(min(list_arrary)))
------------------------------------------------------------------------------------------------------------------------------------------------------
'''