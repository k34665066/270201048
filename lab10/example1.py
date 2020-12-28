def func(n):
    if n==1:
        return 3
    else:
        return  (3 + func(n-1))
print(func(5))
