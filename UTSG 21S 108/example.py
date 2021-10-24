from typing import TextIO, Dict

def create_student_marks(file: TextIO) -> Dict[str, Dict[str, float]]:
    '''
    >>> f = open('grades.csv', 'r')
    >>> student_marks = create_student_marks(f)
    >>> student_marks == {'alice': {'CSC108': 95.0, 'MAT137': 60.0},
    ...                   'vincent': {'CSC108': 73.0}, 
    ...                   'brian': {'BIO100': 50.0}}
    True
    '''

    file.readline() # skip the first header line


    student_marks = {}

    for line in file:
        name, course, grade = line.strip().split(',')

        # -------------
        if name in student_marks:
            student_marks[name][course] = float(grade)
        else:
            student_marks[name] = {course: float(grade)}
        # -------------

    return student_marks

f = open('grades.csv', 'r')
print(create_student_marks(f))
f.close()

## res -> { 'alice' : {'CSC108': 95.0, _____: _____},
#           'vincent': {'CSC108': 73.0},
# }

(1 + 2,)
1 + 2