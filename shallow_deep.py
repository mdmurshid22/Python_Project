a = {'a' : 'k', 7.5 : "idiot", True : False, 6+7J : 45}

b = a[::]

print(a)

print(b)

b[7.5] = [6, 9, True, False, 6+9J, 5-6j, 4*1J]

print('A:',a)

print('B:',b)