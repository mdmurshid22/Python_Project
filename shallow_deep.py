a = {'a' : 'k', 7.5 : "idiot", True : False, 6+7J : 45}
b = a.copy() 
print(a)
print(b)
a[7.5] = [6, 9, True, False, 6+9J]
print(a)
print(b)