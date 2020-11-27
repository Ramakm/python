class Employee:
  def __init__(self, name):
    self.name = name
    print(f'{self.name} is an employee')

class Manager(Employee):
  def __init__(self, department, name):
    self.department = department
    self.name = name
    super().__init__(name)
    print(f'Manager, {self.department} department')

staff_1 = Manager('HR', 'Andy')