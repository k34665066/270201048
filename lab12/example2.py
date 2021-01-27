import math
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def display_information(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
class Company:
    def __init__(self,employee_list):
        self.employee=employee_list
    def get_list(self):
        return self.employee
    def set_list(self,list):
        self.employee=list
    def add_employee(self,new_employee):
        if isinstance(new_employee,self.employee):
            self.employee.append(new_employee)
    def average_salary(self):
        total=0
        num_of_employee=0
        for i in self.employee:
            total+=i.get_salary()
            num_of_employee+=1
        average=total//num_of_employee
        return average
    def display_all_employess(self):
        for i in self.employee:
            i.display_information()


person1=Employee("Esra",1000)
person2=Employee("Murat",5000)
person3=Employee("Eyşan",3000)
employee_list=[person1,person2,person3]
Company1=Company(employee_list)
Company1.average_salary()

