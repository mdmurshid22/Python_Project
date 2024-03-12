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