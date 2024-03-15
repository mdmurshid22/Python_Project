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
class Country:
	my_town = "Neravy"
	my_city = "Karaikal"
	my_state = "Puducherry"
	my_country = "Indian"
c1 = Country()
print("My Home Twon is:{} city:{} state:{} and country:{}".format(c1.my_town,c1.my_city,c1.my_state,c1.my_country))
c2 = Country()
print()
print("My Home Twon is:{} city:{} state:{} and country:{}".format(c1.my_town,c1.my_city,c1.my_state,c1.my_country))
--------------------------------------------------------------------------------------------------------------------------------------
class Students:
	def __init__(self,std_no,std_name,std_mark,std_addr):
		self.std_no = std_no
		self.std_name = std_name
		self.std_mark = std_mark
		self.std_addr = std_addr
s1 = Students(22,'idiot',89,'pavai')
s2 = Students(33,'kk',78,'karai')
print("Student Number:{} Name:{} Mark:{} and Address:{}".format(s1.std_no,s1.std_name,s1.std_mark,s1.std_addr))
print("Student Number:{} Name:{} Mark:{} and Address:{}".format(s2.std_no,s2.std_name,s2.std_mark,s2.std_addr))
--------------------------------------------------------------------------------------------------------------------------------------
s = input('enter any string:')
sp = s.split(' ')
i = -1
l = -len(sp)
l1 = []
while i >= l:
	l1.append(sp[i])
	i-=1
print(s)
for x in l1:
	print(x,end=" ")
--------------------------------------------------------------------------------------------------------------------------------------
a=[15,4,8,14,6,1]
for j in range(len(a)-1): #4
     for i in range(len(a)-1):#4
         if a[i]>a[i+1]:
             a[i],a[i+1]=a[i+1],a[i]
--------------------------------------------------------------------------------------------------------------------------------------
a = eval(input('Enter Any List:'))
i = -1
l = []
le = -len(a)
while i >= le:
	l.append(a[i])
	i-=1
print(a)
print(l)
--------------------------------------------------------------------------------------------------------------------------------------
#Both class and instance atttributes.
class Details:
	country = 'Indian'
	state  = 'Puducherry'
	city = 'Karaikal'
	town = 'Neravy'
	def __init__(self,name,age,mark):
		self.name = name
		self.age = age
		self.mark = mark
d1 = Details('Idiot',19,89)
print("My Name:{} age:{} and Mark:{} Town:{} City:{} State:{} Country:{}".format(d1.name,d1.age,d1.mark,d1.town,d1.city,d1.state,d1.country))
d2 = Details('K',20,891)
print("My Name:{} age:{} and Mark:{} Town:{} City:{} State:{} Country:{}".format(d2.name,d2.age,d2.mark,d2.town,d2.city,d2.state,d2.country))
print(vars(d1))
print(vars(d2))
print(dir(d1))
print(dir(d2))
---------------------------------------------------------------------------------------------------------------------------------------
'''