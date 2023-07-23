class Employee:
    def __init__(self, name, age, salery):
        self.name = name 
        self.age = age
        self.salery = salery 

    def __repr__(self) -> str:
        return f"{self.name}, {self.age}, {self.salery}"

emp_1 = Employee("Driver", 7, 135)
emp_2 = Employee("Steve", 50, 225000)
emp_3 = Employee("Layla", 15, 22500)
emp_4 = Employee("Addi", 14, 21500)
employees = [emp_1, emp_2, emp_3, emp_4]
# print(employees)

def emp_sort(emp):
    return emp.salery

sorted_employees = sorted(employees, key=emp_sort)
print(sorted_employees)

# lambda lambda lambda
sorted_employees = sorted(employees, key= lambda x: x.name)
print(sorted_employees)


from operator import attrgetter

sorted_employees = sorted(employees, key=attrgetter('age'))
print(sorted_employees)

