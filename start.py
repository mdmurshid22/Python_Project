'''class Person:
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
b.home2()'''