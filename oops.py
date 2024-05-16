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
print(c.mt(80,78))"""

class std:
	a=99
	def __init__(self):
		self.b = 88

s = std()
print(s.a)
print(s.b)
s.a = 98
print(s.a)
print(s.b)