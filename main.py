from vehicle import Vehicle, SchoolBus
from employee import Employee
from schools import Student, SchoolOne, SchoolTwo
from vector import Vector
from book_author import Author, Book

print("--- Question 1: Vehicle and School Bus ---")
sb = SchoolBus("Toyota", "Supra", 40)
print(sb.drive())
print("Is SchoolBus a Vehicle?", isinstance(sb, Vehicle))

print("\n--- Question 2: Employee Multiple Constructors ---")
e1 = Employee("Johnson", 25)
e2 = Employee.from_string("Bob-35")
e3 = Employee.default_employee()
print(e1)
print(e2)
print(e3)

print("\n--- Question 3: Schools and GPA ---")
students_one = [Student("John", [90, 80, 85]), Student("Jane", [70, 75, 72])]
school_one = SchoolOne(students_one)
school_one.display()

students_two = [Student("Mike", [88, 90, 85]), Student("Anna", [65, 60, 70])]
school_two = SchoolTwo(students_two)
school_two.display()

print("\n--- Question 4: Vector Operator Overloading ---")
v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)

print("\n--- Question 5: Book and Author Composition ---")
author = Author("George R.R Martin", "an American author, television writer, and television producer. He is best known as the author of the series of epic fantasy novels A Song of Ice and Fire")
book = Book("A Song of Ice and Fire", author)
print(book.get_details())
