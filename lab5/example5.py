
fibonacci_list=list()
fibonacci_list.append(1)
fibonacci_list.append(1)
index=2
how_many=int(input("How many fibonacci numbers do you see?"))
for a in range(how_many-2):
    fibonacci_list.append(fibonacci_list[index-1]+fibonacci_list[index-2])
    index+=1
print(fibonacci_list)