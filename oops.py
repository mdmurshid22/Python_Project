"""class k:
	'''This is my idiot name''' 
	#this is a documentation string. 

murshid = k()
idiot = k()
murshid.name = 'm'
idiot.name = 'h'
print('This is:',idiot.name)
print(murshid.__dict__)
print(k.__doc__)
class student:
	'''This is a constractor by using init method and self keyword.
	constractor is a special function.
	when the object is creation contractor will executed automatically
	python contain default constractor'''
	#static variables / class specific variables.
	sch_name = 'Kamalia high school'
	sch_addr = "Neravy"
	def __init__(self, na, age, address):
		self.name = na
		self.age = age
		self.address = address
		print('Constractor!')

class curtomer():
	'''Method specifin information by using local variables.'''
	def mt(self, amt, bal):
		self.amount = amt
		self.balance = bal
		print('Amount is:', self.amount)

s = student('idiot', 20, 'pavai')
print(s.age)
print(s.__dict__)
print(s.__doc__)
s1 = student('k', 21, 'karai')
print(s1.name)
s.sch_name = 'Kaveri high school'
s1.sch_addr = 'Karaikal'
print(s.sch_name)
print(s1.sch_name)
print()
print(student.sch_addr)
print(student.sch_name)
print(s1.sch_addr)
c = curtomer()
print(s.sch_addr)
#s.mt(66)
print(c.mt(80,78))

class std:
	a=99
	def __init__(self):
		self.b = 88

	def dd(self):
		'''This is Instance Method'''
		self.c = 76
		print('Marks:', self.c)
		print('Ins:', self.a)

s = std()
print(s.a)
print(s.b)
#s.a = 98
print(s.a)
print(s.b)
s.dd()

class ins():
	sch = 'Kamalia high school'
	sch_addr = 'Neravy'
	'''This is class level variables / static variavles.'''
	def mm(self, name, age, mark):
		a = 909090
		sch = 'Khs'
		sch_addr = 'Karaikal'
		print('Name: {} Age: {} Mark: {} School name: {} Address: {} a : {}'.format(name, age, mark, sch, sch_addr, a))

	def kk(self, name, age, mark):
		print('Name: {} Age: {} Mark: {} School name: {} Address: {}'.format(name, age, mark, self.sch, self.sch_addr))
i = ins()
i.mm('idiot', 23, 354)
i.kk('kd', 24, 600)

class clss:
	'''This is class methods
	class method can access only class level variables/static variables
	by using cls variables
	and then use @classmethod
	can call callmethod by using both class name and objects'''
	a = 20
	b = 30
	@classmethod
	def dd(cls, name, total):
		g = 67 
		cls.n = name
		cls.t = total
		print(cls.n, cls.t, cls.a, cls.b)
clss.dd('idiot', 354)
c = clss()
c.dd('k', 366)
print(clss.__doc__)

class met:
	a = 9
	''' This is static method / utility method.
	It access both local and class level variables.
	and by using decorator symbols like.
	@staticmethod and no self and cls varaibles'''
	@staticmethod
	def dis():
		b = 8
		print('This is static method!', b)

m = met()
m.dis()
class met:
	a = 9
	def dis(self):
		self.b = 8
		print('This is static method!', self.a + self.b)

m = met()
m.dis()

class met:
	a = 9
	@classmethod
	def dis(cls):
		cls.b = 8
		print('This is static method!', cls.a + cls.b)

m = met()
m.dis()"""

class students:
	''' student class data here.'''
	def __init__(self, std_name, std_class, std_tamil_mark, std_english_mark, std_maths_mark, std_science_mark, std_social_mark):
		self.std_name = std_name
		self.std_class = std_class
		self.std_tamil_mark = std_tamil_mark
		self.std_english_mark = std_english_mark
		self.std_maths_mark = std_maths_mark
		self.std_science_mark = std_science_mark
		self.std_social_mark = std_social_mark
		print("Student Name:{} and Class:{}".format(self.std_name, self.std_class),end=" ")
		print("Tamil:", self.std_tamil_mark)
		print("English:", self.std_english_mark)
		print("Maths:", self.std_maths_mark)
		print("Science:", self.std_science_mark)
		print("Social:", self.std_social_mark)

Total = int(input("How many student data do you want:"))
for std in range(Total):
	std_name = input("Enter Student Name:")
	std_class = int(input("Enter Student class between 1ts standard to 10th stardrad:"))
	std_tamil_mark = input("Enter Tamil Mark:")
	std_english_mark = input("Enter English Mark:")
	std_maths_mark = input("Enter Maths Mark:")
	std_science_mark = input("Enter Science Mark:")
	std_social_mark = input("Enter Social Mark:")
	std = students(std_name, std_class, std_tamil_mark, std_english_mark, std_maths_mark, std_science_mark, std_social_mark)