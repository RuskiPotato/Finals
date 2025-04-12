# schools.py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def gpa(self):
        avg = self.average()
        if avg >= 90:
            return 4.0
        elif avg >= 80:
            return 3.0
        elif avg >= 70:
            return 2.0
        elif avg >= 60:
            return 1.0
        else:
            return 0.0

class SchoolOne:
    def __init__(self, students):
        self.students = students

    def display(self):
        print("School One - Students:")
        for student in self.students:
            print(f"{student.name} - Average: {student.average():.2f}, GPA: {student.gpa():.2f}")

class SchoolTwo:
    def __init__(self, students):
        self.students = students

    def display(self):
        print("School Two - Students:")
        for student in self.students:
            print(f"{student.name} - Average: {student.average():.2f}, GPA: {student.gpa():.2f}")
