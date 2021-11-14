# Relationship
#  Inheritance (Is-A relationship)
#     class subClass(SuperClass)
#     class ChildClass(ParentClass)
#     class DerivedClass(BaseClass)

#  Association
#   Class A is associated with Class B, if Class A uses Class B in any of the following way:
#     - Class A has method(s) that takes an object of type B
#     - Class A has method(s) that return an object of type B


#     - Class A has attribute(s) of type B

#    Composition - strong Association (Part-Of relationship)
#
#        class Room:
#
#        class House:
#             bed_room: Room       * room cannot exist by itself
#

#    Aggregation - weak Association (Has-A relationship)
#
#        class Vehicle:
#             engine: Engine
#             brake: Brake
#             windows: list[Window]



# Other Useful Built-In Method
# a == b        __eq__
# a != b        __ne__
# a > b         __gt__
# a >= b        __ge__
# a < b         __lt__
# a <= b        __le__
# len(a)        __len__
# a in b:       __contains__

from __future__ import annotations

# Parent Class (Base class, Super Class)
class Person:
    """A Person, a class to represent a human being."""

    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other: Person) -> bool:
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.age == other.age

    def __len__(self) -> int:
        return len(self.first_name) + len(self.last_name)

    def __str__(self) -> str:
        return f'Hello I am {self.first_name} {self.last_name} ' \
               f'I am {self.age} years old :)'

    def eat(self, food: str) -> str:
        return f'Yummy! {self.first_name} is eating {food}!!!'

    def give_birth(self, husband: Person, first_name: str) -> Person:
        # do something bad bad XXXOOOOO
        return Person(first_name, husband.last_name, 1)


# Child Class (Derived Class, Sub Class)
class Student(Person):

    student_number: str

    def __init__(self, first_name: str, last_name: str, age: int, student_number: str) -> None:
        Person.__init__(self, first_name, last_name, age)
        self.student_number = student_number

    # Method Override
    def __str__(self):
        return super().__str__() + f' and my student number is: {self.student_number}'


    def enroll(self, course: Course) -> None:
        course.add_student(self)

class Professor(Person):
    """
    """


class Course:

    course_code: str
    professor: Professor
    students: list[Student]

    def __init__(self, course_code, professor):
        self.course_code = course_code
        self.professor = professor
        self.students = []

    def add_student(self, student: Student):
        self.students += [student]


vc = Person('Vincent', 'Tse', 18)  # Person.__init__(vc, 'Vincent', 'Tse', 18)

# print(Person.eat(vc, 'Fish'))
print(vc.eat('Fish'))

a = Person('Alice', 'Chen', 24)

print(vc == a)  # Person.__eq__(vc, a) -> vc.__eq__(a)
print(len(vc))  # Person.__len__(vc)

print(vc)       # Person.__str__(vc)

son = a.give_birth(vc, 'Vinson')
print(son)


s1 = Student('David', 'Liu', 10, '123456789')
# Student.__init__(s1, 'David', 'Liu', 10, '123456789')
print(s1) # Student.__str__(s1)


bob = Professor('Bob', 'Tse', 70)

csc110 = Course('CSC110', bob)

s1.enroll(csc110)




