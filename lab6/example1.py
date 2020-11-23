email=input("Please enter email adress:")
example="ceng113@example.com"
emailrevised=""
index=email.index("@")
for i in email[0:index]:
    if i==".":
        continue
    else:
        emailrevised+=i
for  j in email[index:]:
    emailrevised +=j
if email.lower() == example or email.upper() == example or emailrevised.upper() == example or emailrevised.lower() == example:
        print("TRUE")
else:
        print("false")

