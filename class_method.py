class Employee:
    company="camel"
    salary=100
    location="kolkata"

    @classmethod
    def salaryChange(cls,sal):
        cls.salary= sal

e = Employee()
print(e.salary)
e.salaryChange(400)
print(e.salary)
print(Employee.salary)