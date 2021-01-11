class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_salary(self):
        return self.salary
    def get_name(self,name):
        return self.name
    def set_name(self,name):
        self.name=name
    def set_salary(self,salary):
        if salary>0:
            self.salary=salary
    def display(self):
        print(f"Name:{self.name}  Salary:{self.salary}")
class Company:
    def __init__(self):
        self.employeelist=[]
    def get_employee(self):
        return self.employeelist
    def set_employee(self,current_list):
        if type(current_list)==list:
            self.employeelist=current_list
    def add_employee(self,new_employee):
        if isinstance(new_employee,Employee):
            self.employeelist.append(new_employee)
    def calc_avg_salary(self):
        total_sum=0
        for emp in self.employeelist:
           total_sum+=emp.get_salary()
        return total_sum/len(self.employeelist)
    def display(self):
        for emp in self.employeelist:
            print(f"Name:{emp.get_name()}")
            print((f"Salary{emp.get_salary()}"))

c=Company()
e1=Employee("cem",4000)
e2=Employee("merve",4000)
e3=Employee("gamze",4000)
e4=Employee("can",4000)
c.add_employee(new_employee=e1)
c.add_employee(new_employee=e2)
c.add_employee(new_employee=e3)
c.add_employee(new_employee=e4)
c.display()