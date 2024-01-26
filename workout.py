outer=int(input('Enter Outer-Loop Number:'))
inner=int(input('Enter Inner-Loop Number:'))
i=1
j=1
while i <= outer:
	print(i,'Outer_Loop')
	while j <= inner:
		print(j,'Inner_Loop')
		j+=1
	j=1
	i+=1