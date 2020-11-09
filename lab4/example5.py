n_value = int(input("Please enter the n value:"))
factorial = 1
for i in range(1, n_value + 1):
    factorial *= i
    n_value-=1

print(factorial)


