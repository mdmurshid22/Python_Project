#inner=int(input('Enter Inner-Loop Number:'))
#outer=int(input('Enter Outer-Loop Number:'))
i=1
j=1
while i <= 5:
	print(i,'Outer_Loop')
	while j <= 5:
		print(j,'Inner_Loop')
		j+=1
	j=1
	i+=1