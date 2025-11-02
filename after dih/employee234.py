class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

employee1 = Employee("Alice", 30, "Engineer")
employee2 = Employee("Bob", 25, "Designer")

employee1.display_info()
employee2.display_info()



