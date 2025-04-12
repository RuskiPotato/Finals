class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, emp_str):
        name, age = emp_str.split("-")
        return cls(name, int(age))

    @classmethod
    def default_employee(cls):
        return cls("John Doe", 30)

    def __str__(self):
        return f"Employee: {self.name}, Age: {self.age}"