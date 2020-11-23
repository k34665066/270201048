
gradelist=list()
how_many_students=int(input("How many students:"))

for i in range(how_many_students):
    midterm_1=int(input("Please enter the midterm 1 grade:"))
    midterm_2=int(input("Please enter the midterm 2 grade:"))
    final=int(input("Please enter the final grade:"))
    average=midterm_1*(3/10)+midterm_2*(3/10)+final*(4/10)
    examlist=list()
    examlist.append(midterm_1)
    examlist.append(midterm_2)
    examlist.append(final)
    gradelist.append(examlist)
print(gradelist)
