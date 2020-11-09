a_first=int(input("Please enter the base"))
b=int(input("Please enter the exponent" ))
a=a_first
for i in range(b-1):
	a*=a_first
print(a)