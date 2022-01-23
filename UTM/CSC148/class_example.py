from __future__ import annotations
from random import randint
from typing import Optional, Union

class Person:
    """A Person.

    === Attributes ===
    name:
        The name of the person
    age:
        The age of the person
    gender:
        The gender of the person
    
    === Representation Invariant ===
    age > 0
    gender in ('F', 'M')

    """
    name: str
    gender: str
    age: int

    def __init__(self, name: str, age: int, gender: str) -> None:
        """Initialize a new person with <name> name and <age> age.

        Precondition: 
            age > 0
            gender in ('F', 'M')
        """
        self.name = name
        self.age = age
        self.gender = gender
    
    def __gt__(self, other: Person) -> bool:
        """Return True iff this person is older than the other person.
        """
        return self.age > other.age
    
    def __str__(self) -> str:
        """Return the string representation of a Person.
        """
        return f'{self.name}, {self.age}'
    
    def eat(self, food: str) -> str:
        """Return a string that representing the person is eating.
        """
        return f'{self.name} is eating {food}...'
    
    def give_birth(self, husband: Person, child_name: str) -> str:
        """:)
        """
        assert self.gender == 'F'
        assert husband.gender == 'M'
        assert self.age >= 18
        assert husband.age >= 18

        child = Person(child_name, 1, 'F' if randint(0, 1) == 0 else 'M')
        return child


class Student(Person):
    """A student.
    """

    utorid: str
    # courses: list[Course]
    courses: dict[Course, Optional[Grade]]

    def __init__(self, name: str, age: int, gender: str, utorid: str) -> None:
        Person.__init__(self, name, age, gender)
        self.utorid = utorid
        self.courses = {}

    
    def __str__(self) -> str:
        return f'{self.utorid}: {Person.__str__(self)}'
    
    def enroll(self, course: Course) -> bool:
        if course.enroll(self):
            # self.courses.append(course)
            self.courses[course] = None
            return True
        else:
            return False

    def add_grade(self, course: Course, mark: Union[str, float]) -> None:
        if course in self.courses:
            if isinstance(mark, float):
                self.courses[course] = NumericGrade(mark)
            else:
                self.courses[course] = LetterGrade(mark)
    

    def cgpa(self) -> float:
        if len(self.courses) == 0:
            return 0.0

        total_gpa = 0
        for course in self.courses:
            grade = self.courses[course] # NumericGrade or LetterGrade ..
            total_gpa += grade.gpa()
        
        return total_gpa / len(self.courses)

class Course:
    
    course_code: str
    capacity: int
    students: list[Student]
    waiting_list: list[Student]
    instructor: Instructor

    def __init__(self, course_code: str, capacity: int, instructor: Instructor):
        self.course_code = course_code
        self.capacity = capacity
        self.students = []
        self.waiting_list = []
        self.instructor = instructor
        instructor.add_course(self)

    def enroll(self, student: Student) -> bool:
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        else:
            self.waiting_list.append(student)
            return False
    
    def __str__(self) -> str:
        res = ''
        res += f'{self.course_code} {len(self.students)}/{self.capacity}\n'
        res += f'Instructor:\n  {self.instructor}\n'
        res += 'students:\n'
        for student in self.students:
            res += f'  {str(student)}\n'
        res += 'waiting_list:\n'
        for student in self.waiting_list:
            res += f'  {str(student)}\n'
        
        return res
        

class Faculty:
    """"""

    empID: int

    def __init__(self, empID: int) -> None:
        self.empID = empID

    def get_salary(self) -> float:
        raise NotImplementedError


class Instructor(Person, Faculty):

    courses: list[Course]

    def __init__(self, name: str, age: str, gender: str, empID: int) -> None:
        Person.__init__(self, name, age, gender)
        Faculty.__init__(self, empID)
        self.courses = []
    
    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def get_salary(self) -> float:
        return 10000 * len(self.courses)


class StudentTA(Student, Faculty):

    hours: int

    def __init__(self, name: str, age: str, gender: str, utorid: str, empID: int) -> None:
        Student.__init__(self, name, age, gender, utorid)
        Faculty.__init__(self, empID)
        self.hours = 0
    
    def teach(self, hours: int) -> None:
        self.hours += hours

    def get_salary(self) -> float:
        return self.hours * 44


class Grade:    
    def gpa(self) -> float:
        raise NotImplemented

class NumericGrade(Grade):
    mark: float

    def __init__(self, mark: float) -> None:
        self.mark = mark

    def gpa(self) -> float:
        if self.mark >= 85:
            return 4.0
        elif self.mark >= 80:
            return 3.7
        elif self.mark >= 77:
            return 3.3
        elif self.mark >= 74:
            return 3.0
        elif self.mark >= 70:
            return 2.7
        elif self.mark >= 67:
            return 2.3
        elif self.mark >= 64:
            return 2.0
        elif self.mark >= 60:
            return 1.7
        elif self.mark >= 57:
            return 1.3
        elif self.mark >= 54:
            return 1.0
        elif self.mark >= 50:
            return 0.7
        else:
            return 0.0

class LetterGrade(Grade):
    mark: str

    def __init__(self, mark: str) -> None:
        self.mark = mark
    
    def gpa(self) -> float:
        if self.mark == 'A' or self.mark == 'A+':
            return 4.0
        elif self.mark == 'A-':
            return 3.7
        elif self.mark == 'B+':
            return 3.3
        elif self.mark == 'B':
            return 3.0
        elif self.mark == 'B-':
            return 2.7
        elif self.mark == 'C+':
            return 2.3
        elif self.mark == 'C':
            return 2.0
        elif self.mark == 'C-':
            return 1.7
        elif self.mark == 'D+':
            return 1.3
        elif self.mark == 'D':
            return 1.0
        elif self.mark == 'D-':
            return 0.7
        else:
            return 0.0


if __name__ == "__main__":

    cora = Person('Cora', 18, 'F')
    david = Person('David', 19, 'M')
    
    print(cora.name)
    print(cora)
    print(david > cora) # Person.__gt__(bob, alice)
    covid = cora.give_birth(david, 'covid')

    # ------------------------------
    print()
    print()


    s1 = Student("alice", 18, "F", "a123")
    s2 = Student("bob", 18, "M", "b123")
    s3 = Student("carol", 18, "F", "c123")

    print(s1 > s2)
    print(s1)
    print(s2)

    vc = Instructor("vincent", 20, 'M', 111)

    csc148 = Course("CSC148", 2, vc)
    csc165 = Course("CSC165", 3, vc)
    csc209 = Course("CSC209", 10, vc)
    s1.enroll(csc148)
    s1.enroll(csc165)
    s2.enroll(csc148)
    s3.enroll(csc148)
    print(csc148)

    
    ta = StudentTA('Eric', 22, 'M', 'e123', 222)
    ta.teach(65)
    ta.enroll(csc209)
    print(csc209)


    print(vc.get_salary())
    print(ta.get_salary())


    s1.add_grade(csc148, 'A+')
    s1.add_grade(csc165, 78.8)

    print(s1.cgpa())









    