year=int(input("Please enter the year:"))
if year%4==0 and year%400!=0:
	print("It is not leap years")
elif year%4==0 and year%400==0:
	print("It is leap years")