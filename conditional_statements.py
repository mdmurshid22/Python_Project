#1 Find the greatest number of given three nuumber?
'''num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
if (num1 > num2) & (num1 > num3):
	print("First Numbers is Greater:",num1)
elif num2>num3:
	print("Second Number is Greater:",num2)
else:
	print("Third Number is Greater:",num3)'''

#2 Polindrome?
'''s=input("Enter Some String:")
s1=s[::-1]
if s == s1:
	print("It is Polindrome:",s)
else:
	print("It is not a Polindrome:",s)'''

#3 Voting?
'''age=int(input("Enter Your Age:"))
if age >= 18:
	print("You are Eligible for voting:",age)
else:
	print("You are not Eligible for Voting:",age)'''

#4 Pass or Fail program?
'''tamil=int(input("Enter Tamil Mark:"))
english=int(input("Enter English Mark:"))
maths=int(input("Enter Maths Mark:"))
science=int(input("Enter Science Mark:"))
social=int(input("Enter Social Mark:"))
if tamil >=35:
	if english >=35:
 		if maths >=35:
 			if science >=35:
 				if social >=53:
 					print("Tamil:{} pass\nEnglish:{} pass\nMaths:{} pass\nScience:{} pass\nSocial:{} pass".format(tamil,english,maths,science,social))
 					print("Total Marks:{}".format(tamil+english+maths+science+social))
 					print("Percentage of All Subjects is:{:.1f}%".format(tamil,english,maths,science,social/500*100))
else:
	print("Fail\nTamil:{}\nEnglish:{}\nMaths:{}\nScience:{}\nSocial:{}".format(tamil,english,maths,science,social))'''
'''import math
d=dir(math)
for x in d:
	print(x)'''
"""num=int(input("How Many Students Marks Do You Want:"))
list=["Tamil","English","Maths","Science","Social"]
for i in range(num):
	l=[]
	student_name=input("Enter Student Name:")
	for x in range(5):
		subject=int(input("Enter {} Mark:".format(list[x])))
		l.append(subject)
		output=sum(l)
		if l[x] >= 35:
			print("Pass {} subject {}".format(l[x],list[x]))
		else:
			print("Fail {} subject {}".format(l[x],list[x]))
	print("Total Marks {} By {}".format(output,student_name))
	print()"""
"""n=int(input("Enter Any Number 1 to 7:"))
if n == 1:
	print("Sunday")
elif n == 2:
	print("Monday")
elif n == 3:
	print("Tuesday")
elif n == 4:
	print("Wednesday")
elif n == 5:
	print("Thursday")
elif n == 6:
	print("Friday")
elif n == 7:
	print("Saturday")
else:
	print("Invalid!")
city_name=input("Enter Your City Name:")
city=city_name.strip()
if city.upper() == "KARAIKAL":
	print("KARAIKAL IS GOOD")
elif city.upper() == "NAGORE":
	print("NAGORE IS TOO GOOD")
elif city.upper() == "NAGAPATTINAM":
	print("NAGAPATTINAM IS VERY GOOD")
else:
	print("INVALID CITY!")"""
'''degree_name=input("Enter Any degree[ENGINEERING,ARTS AND SCIENCE,DIPLOMA]: ")
degree=degree_name.strip()
if degree.upper() == "ENGINEERING":
	department_name=input("Enter Any Department of Engineering[MECH,EEE,ECE,CSC]:")
	department=department_name.strip()
	if department.upper() == "MECH":
		print("BOYS ONLY!")
	elif department.upper() == "EEE":
		print("BOTH BOYS AND GIRLS")
	elif department.upper() == "ECE":
		print("GIRLS ONLY")
	elif department.upper() == "CSC":
		print("FUN ONLY")
	else:
		print("INVALID DEPARTMENT")
elif degree.upper() == "ARTS AND SCIENCE":
	department_name=input("Enter Any Department of Arts and Science[BCA,BSC,CS,BBA]:")
	department=department_name.strip()
	if department.upper() == "BCA":
		print("BOYS ONLY!")
	elif department.upper() == "BSC":
		print("BOTH BOYS AND GIRLS")
	elif department.upper() == "CS":
		print("GIRLS ONLY")
	elif department.upper() == "BBA":
		print("FUN ONLY")
	else:
		print("INVALID DEPARTMENT")
elif degree.upper() == "DIPLOMA":
	department_name=input("Enter Any Department Diploma[MECH,EEE,ECE,CSC]:")
	department=department_name.strip()
	if department.upper() == "MECH":
		print("BOYS ONLY!")
	elif department.upper() == "EEE":
		print("BOTH BOYS AND GIRLS")
	elif department.upper() == "ECE":
		print("GIRLS ONLY")
	elif department.upper() == "CSC":
		print("FUN ONLY")
	else:
		print("INVALID DEPARTMENT")
else:
	print("INVALID DEGREE!")'''
"""slipper_name=eval(input("Enter Any List of 3 Slipper Name:"))
for slip in range(2):
	print("{} = {}".format(slipper_name[slip],2))
i=""
while i < slipper_name[2]:
	print("{} = {}".format(slipper_name[2],1))
	break"""