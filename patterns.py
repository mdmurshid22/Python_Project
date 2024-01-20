alphabet = input("Enter Any Alphahet:")
if alphabet == 'A' or alphabet == 'a':
	for i in range(4):
		for j in range(7):
			if i == 0:
				if j == 3:
					print(alphabet,end="")
				else:
					print(" ",end="")
			elif i == 1:
				if j == 2 or j == 4:
					print(alphabet,end="")
				else:
					print(" ",end="")
			elif i == 2:
				if j == 0 or j == 6:
					print(" ",end="")
				else:
					print(alphabet,end="")
			elif i == 3:
				if j == 0 or j == 6:
					print(alphabet,end="")
				else:
					print(" ",end="")
		print()
elif alphabet == 'B' or alphabet == 'b':
	for i in range(9):
		for j in range(4):
			if i == 0:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 8:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'C' or alphabet == 'c':
	for i in range(7):
		for j in range(5):
			if i == 0:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print("  ",end=" ")
			elif i == 3:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			if i == 6:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'D' or alphabet == 'd':
	for i in range(6):
		for j in range(4):
			if i == 0:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0 or j == 3:
					print(alphabet,end="")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'E' or alphabet == 'e':
	for i in range(5):
		for j in range(4):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				print(alphabet,end=" ")
			elif i == 3:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				print(alphabet,end=" ")
		print()
elif alphabet == 'F' or alphabet == 'f':
	for i in range(5):
		for j in range(4):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				print(alphabet,end=" ")
			elif i == 3:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'G' or alphabet == 'g':
	for i in range(7):
		for j in range(6):
			if i == 0:
				if j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 2 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 1 or j == 5:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 4:
				if j == 0 or j == 2 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 0 or j == 2 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j ==0 or j == 3 or j == 5:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
		print()
elif alphabet == 'H' or alphabet == 'h':
	for i in range(5):
		for j in range(4):
			if i == 0:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				print(alphabet,end=" ")
			elif i == 3:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'I' or alphabet == 'i':
	for i in range(5):
		for j in range(5):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				print(alphabet,end=" ")
		print()
elif alphabet == 'J' or alphabet == 'j':
	for i in range(6):
		for j in range(5):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 0 or j == 1 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'K' or alphabet == 'k':
	for i in range(5):
		for j in range(4):
			if i == 0:
				if j == 1 or j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 1:
				if j == 1 or j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 2:
				if j == 0 or j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 1 or j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 4:
				if j == 1 or j ==2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
		print()
elif alphabet == 'L' or alphabet == 'l':
	for i in range(5):
		for j in range(4):
			if i == 0:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				print(alphabet,end=" ")
		print()
elif alphabet == 'M' or alphabet == 'm':
	for i in range(5):
		for j in range(5):
			if i == 0:
				if j == 0 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 2:
				if j == 1 or j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 3:
				if j == 0 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'N' or alphabet == 'n':
	for i in range(5):
		for j in range(5):
			if i == 0:
				if j == 0 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 2 or j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 2:
				if j == 1 or j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 3:
				if j == 1 or j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 4:
				if j == 0 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'O' or alphabet == 'o':
	for i in range(7):
		for j in range(7):
			if i == 0:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 1 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 1 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			if i == 6:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'P' or alphabet == 'p':
	for i in range(8):
		for j in range(3):
			if i == 0:
				if j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 1:
				if j == 1:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 2 :
				if j == 1:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 3:
				if j == 1:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 4:
				if j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 5:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'Q' or alphabet == 'q':
	for i in range(9):
		for j in range(7):
			if i == 0:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 1 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 0 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 1 or j == 2 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 2 or j == 3 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 8:
				if j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'R' or alphabet == 'r':
	for i in range(9):
		for j in range(4):
			if i == 0:
				if j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 1:
				if j == 1 or j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 2 :
				if j == 1 or j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 3:
				if j == 1 or j == 2:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 4:
					print(alphabet,end=" ")
			elif i == 5:
				if j == 0 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 0 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'S' or alphabet == 's':
	for i in range(7):
		for j in range(4):
			if i == 0:
				if j == 0:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
			elif i == 1:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 1 or j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 3:
					print(" ",end=" ")
				else:
					print(alphabet,end=" ")
		print()
elif alphabet == 'T' or alphabet == 't':
	for i in range(5):
		for j in range(5):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'U' or alphabet == 'u':
	for i in range(5):
		for j in range(6):
			if i == 0:
				if j == 0 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j == 0 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 0 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 1 or j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 2 or j == 3:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'V' or alphabet == 'v':
	for i in range(5):
		for j in range(9):
			if i == 0:
				if j == 0 or j == 8:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j ==1  or j == 7:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 3 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'W' or alphabet == 'w':
	for i in range(5):
		for j in range(17):
			if i == 0:
				if j == 0 or j == 8 or j == 16:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j ==1  or j == 7 or j == 9 or j == 15:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2 or j == 6 or j == 10 or j == 14:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 3 or j == 5 or j == 11 or j == 13:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 4 or j == 12:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'X' or alphabet == 'x':
	for i in range(9):
		for j in range(9):
			if i == 0:
				if j == 0 or j == 8:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j ==1  or j == 7:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 3 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 3 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 2 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 1 or j == 7:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 8:
				if j == 0 or j == 8:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'Y' or alphabet == 'y':
	for i in range(8):
		for j in range(9):
			if i == 0:
				if j == 0 or j == 8:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 1:
				if j ==1  or j == 7:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 2 or j == 6:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				if j == 3 or j == 5:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 4:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 5:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 6:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 7:
				if j == 4:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
		print()
elif alphabet == 'Z' or alphabet == 'z':
	for i in range(4):
		for j in range(4):
			if i == 0:
				print(alphabet,end=" ")
			elif i == 1:
				if j == 2:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 2:
				if j == 1:
					print(alphabet,end=" ")
				else:
					print(" ",end=" ")
			elif i == 3:
				print(alphabet,end=" ")
		print()