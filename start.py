'''
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def home(self):
		print('Good Evening!')
class Per(Person):
	def __init__(self,name,age,address):
		super().__init__(name,age)
		self.address=address
	def home(self):
		print(self.name,self.age)
	def home1(self):
		print(self.address)
b=Per('idiot',22,'karaikal')
b.home()
b.home1()
-------------------------------------------------------------------------------------------------------------------------------------
class Person:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def home(self):
		print(self.a+self.b)
class Per(Person):
	def __init__(self,a,b,c):
		super().__init__(a,b)
		self.c = c
	def home1(self):
		print(self.a+self.b+self.c)
	def home2(self):
		print(self.c)
b=Per(90,int(6),70)
b.home1()
b.home2()
-------------------------------------------------------------------------------------------------------------------------------------
class Students:
	def __init__(self,stdname,stdmark,stdaddr):
		self.stdname = stdname
		self.stdmark = stdmark
		self.stdaddr = stdaddr
s=Students('idiot',98,'karai')
-------------------------------------------------------------------------------------------------------------------------------------
class Student:
	std_name = 'idiot'
	std_no = 22
	std_mark = 354
	std_addr = 'pavai'
	def display(self):
		print('Student Name:',self.std_name)
		print('Student Number:',self.std_no)
		print('Student Mark:',self.std_mark)
		print('Student Address:',self.std_addr)
s1 = Student()
s1.display()
print()
s2 = Student()
s2.display()
print()
print(s1.std_addr)
print(s1.std_mark)
print(s1.std_no)
print(s1.std_name)
-------------------------------------------------------------------------------------------------------------------------------------
'''