# Program that demonstrates multiple inheritance 
# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_Person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# child class
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_Employee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.salary}")  


# child class
class Manager(Person, Employee):

    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_Manager(self):
        print("----- Manager Details -----")
        self.display_Person()
        self.display_Employee()
        print(f"Department: {self.department}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting")


# Creating Object
manager1 = Manager("ABC", 22, "1000", 95000, "IT")

manager1.display_Manager()
manager1.conduct_meeting()        

