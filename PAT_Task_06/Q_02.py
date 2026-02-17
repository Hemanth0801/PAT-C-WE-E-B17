
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_salary(self):
        return self.base_salary

class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, base_salary, bonus, allowance):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.allowance

#object

emp1 = RegularEmployee("Hemanth", 30000, 5000)
emp2 = ContractEmployee("venkat", 500, 80)
emp3 = Manager("Bhaskar", 50000, 10000, 8000)

employees = [emp1, emp2, emp3]

for emp in employees:
    print(f"Employee Name: {emp.name}")
    print(f"Total Salary: {emp.calculate_salary()}")
