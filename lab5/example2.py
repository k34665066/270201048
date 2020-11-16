loop_number=int(input("How many numbers?"))
list_num=list()
list_num2=list()
for i in range(loop_number):
    number=int(input("Enter an integer:"))
    list_num.append(number)
for a in list_num:
        if a %2==0:
            list_num2.append(a)
solution=(len(list_num2)*100)/(len(list_num))
print("%",solution)





