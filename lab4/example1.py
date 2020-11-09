number=(input("Please enter the number:"))
if int(number) in range(10):
	print(int(number))
else:
	print(int(number[-1])+int(number[-2]))
