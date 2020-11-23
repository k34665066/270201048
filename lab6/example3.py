how_many_student=int(input("How many students do you have?:"))
gradelist=list()
for i in range(how_many_student):
  grade=int(input("Enter the grade:"))
  if grade>90:
    gradelist.append(grade)
