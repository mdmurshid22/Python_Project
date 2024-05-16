"""class k:
	'''This is my idiot name''' 
	#this is a documentation string. 

murshid = k()
idiot = k()
murshid.name = 'm'
idiot.name = 'h'
print('This is:',idiot.name)
print(murshid.__dict__)
print(k.__doc__)"""
class student:
	'''This is a constractor by using init method and self keyword.
	constractor is a special function.
	when the object is creation contractor will executed automatically
	python contain default constractor'''
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
		print('Constractor!')

s = student('idiot', 20, 'pavai')
print(s.age)
print(s.__dict__)
print(s.__doc__)
s1 = student('k', 21, 'karai') 