from typing import TextIO


def create_student_marks(f: TextIO) -> dict[str, dict[str, float]]:
    """
    >>> f = open('marks.csv', 'r')
    >>> student_marks = create_student_marks(f)
    >>> f.close()
    >>> student_marks == {'alice': {'CSC108': 99.0, 'MAT137': 80.0},
    ...                   'bob': {'CSC108': 95.0, 'ECO101': 75.0},
    ...                   'vincent': {'CSC110': 50.0}}
    True
    """

    # student_marks -> {'alice': {'CSC108': 99.0, 'MAT137': 80.0}, 
    #                   'bob': {'CSC108': 95.0}}


    # name      -> alice    -> bob      -> alice
    # course    -> CSC108   -> CSC108   -> MAT137
    # grade     -> 99       -> 95       -> 80

    f.readline() # skip the first header line

    student_marks = {}  

    for line in f:
        name, course, grade = line.strip().split(',')

        # # -------------
        # if name in student_marks:
        #     student_marks[name] [course] = float(grade)
        # else:
        #     student_marks[name] = {course: float(grade)}
        # # -------------

        if name not in student_marks:
            student_marks[name] = {}
        student_marks[name] [course] = float(grade)

    return student_marks

