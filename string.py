#A Collection of Characters or Group of Characters within single or double qoutes.
#s="Python is a programming language and easy to programming"
#print(s)
'''sp=s.split()
print(sp)
j=" ".join(sp[::-1])
print(j)
j=" ".join(reversed(sp))
print(j)'''
eno=int(input("Enter Your Employee Number:"))
ename=input("Enter Your Employee Name:")
esalary=float(input("Enter Your Employee Salary:"))
eaddress=input("Enter Your Employee Address:")
print("Employee Number:{} Name:{} Salary:{} and Address:{}".format(eno,ename,esalary,eaddress))
print("Employee Number:{0} Name:{1} Salary:{2} and Address:{3}".format(eno,ename,esalary,eaddress))
print("Employee Number:{no} Name:{na} Salary:{es} and Address:{ed}".format(no=eno,na=ename,es=esalary,ed=eaddress))
print()
print("Employee Number:%i Name:%s Salary:%.2f and Address:%s" %(eno,ename,esalary,eaddress))