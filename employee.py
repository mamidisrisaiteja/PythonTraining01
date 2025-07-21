class Employee:
    def __init__(self,name,salary):

        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, Salary:Rs.{self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)          #Call parent constructor
        self.department=department
    
    def display_manager(self):
        print(f"Manages:{self.department}department")


mgr=Manager("Ravi", 80000, "QA Automation")
mgr.display_info()
mgr.display_manager()

