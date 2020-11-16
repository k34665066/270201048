password="abc123"
while True:
    enter_password = input("Please enter the password:")
    if enter_password==password:
        print("Welcome")
        break
    elif enter_password==("help"):
        print(password[0])
    else:
        print("Wrong")