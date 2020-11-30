"""EMPLOYEES"""


name_salary = {}
salaryvalue = []
namesss = []
for i in range(5):
    name = input("Please enter your name:")
    salary = int(input("Please enter your salary:"))
    namesss.append(name)
    salaryvalue.append(salary)
    name_salary[name] = salary
sortedform=sorted(salaryvalue)
print(name_salary)
max3salary =sortedform[2:]
for i in namesss:
    if name_salary[i] in max3salary:
        print(i,":",name_salary[i])
