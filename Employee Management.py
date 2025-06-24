"""
1. Class Employee created with attributes name,salary and method calculate_salary

2. Inherited the class Employee and created three subclasses Regular Employee,Contract Employee and Manager

3. Polymorphism is applied to the method calculate_salary and it is calculated based on employee type.
It is having specific attributes and rules.
"""


class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_salary(self,grosspay):
        return grosspay

class RegularEmployee(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
    def calculate_salary(self,allowance,deductions):
        return self.salary+ allowance -deductions*1.00

class ContractEmployee(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)

    def calculate_salary( self,TotalworkingDays,Daysworked):
            Dailyrate=self.salary/TotalworkingDays
            return Dailyrate*Daysworked

class Manager(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
    def calculate_salary(self,allowance,deductions):
            return (self.salary+ allowance -deductions)*1.25

print("\n Welcome to Employee Management System \n")
employeename=str(input("Enter Employee Name:"))
employeeType=str(input("Enter Employee Type R-Regular C-Contract M-Manger:"))

if employeeType=="R":
    employee=RegularEmployee(employeename,10000)
    print(f"Salary of {employeename} is Rs.",employee.calculate_salary(10000,2500))
elif employeeType=="C":
    employee=ContractEmployee(employeename,7500)
    totalworkingdays=20
    daysworked=15
    print(f"Salary of {employeename} is Rs.",employee.calculate_salary(totalworkingdays,daysworked))
elif employeeType=="M":
    employee=Manager(employeename,25000)
    print(f"Salary of {employeename} is Rs.",employee.calculate_salary(25000,7500))
else:
    print("Entered invalid Employee Type.")
