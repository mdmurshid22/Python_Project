'''dict={5:8,'k':7+9J,True:False,8:'idiot',5:7,6:7,8:8}
print(dict)
print(type(dict))
print(len(dict))
print(dict[5])
print(dict[8])
print(dict[True])
d=dict[5]='KK'
print(d)
print(dict)
d=dict[5]={1:2,2:3}
print(dict)
print(dict[5][1])
#print(dir(dict))
a={'students':{'name':{'sname':'i','mark':10},'name':{'sname':'j','mark':20}}}
print(a)
b=a['students']['name']='idiot'
print(b)
print(a)
d=a.copy()#Copy all elements from the Dictionay return deep copy. 
print(d)
a.clear()#Remove all elements from the Dictionay return {empty dict}.
print(a)
print(dict.get(99,{8:9,7:9}))#To Get value by using get() method If the specified keys does not exits by default value is return.
print(dict)
print()
kk=dict.keys()
for x in kk:
	print(x)
print()
vv=dict.values()
for x in vv:
	print(x)
print()
dd=dict.items()
for x in dd:
	print(x)
print()
print(dict)
df=dict.update({5:{97:"7"}})#To Update Iterable Object Dictionay, keys-value pairs If the specified keys does not exits Update key-values displayed. 
print(dict)
print(df)
h=dict.setdefault('True',"False1")#Setdefault Method() To set and update the key-value pairs if any key is specified and return the value.
print(h)
print(dict)
keys=True,
value=8
l=dict.fromkeys(keys,value)#Only display key-value, Iterable keys only allowed fromkeys(keys=required,value=optionl, default values is None).
print(l)
print(dict)
g=dict.pop('k')
print(g)
print(dict.pop(False,'none'))#To remove the specified value is return if any key is does not exits raise the KeyError, if you can specified default value also.
print(dict.popitem())#To remove the last key-value is return, popitem(No arguments passed)Methods.
------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
