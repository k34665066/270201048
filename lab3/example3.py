number_of_lecturs=float(input("Please enter number of lectures:"))
gpa=float(input("Please enter GPA:"))

if gpa<2 and number_of_lecturs<47:
	print("Not enough number of lectures and GPA !")
elif gpa<2 and number_of_lecturs>=47:
	print("Not enough GPA!")
elif gpa>=2 and number_of_lecturs<47:
	print("Not enough number of lectures!")
else:
	print("GRADUATED!!!")
	
