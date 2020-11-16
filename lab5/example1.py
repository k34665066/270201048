number=int(input("Please enter the number"))
for i in range(1,11):
    if number<0:
        print("Please enter valid n")
        break
    elif number>10:
        print("Please enter number<10")
        break


    number2=number*i
    print(number,"X",i,"=",number2)