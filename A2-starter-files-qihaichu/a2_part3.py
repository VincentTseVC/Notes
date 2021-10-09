"""CSC110 Fall 2021 Assignment 2, Part 3: Generating a Timetable

Instructions (READ THIS FIRST!)
===============================
This Python module contains the functions you should complete for Part 3 of this assignment.
Your task is to complete the functions in this module, following the definitions given in
the assignment handout.

You may find it useful to write helper functions to split up your code (we've provided
some hints on places to do so below).

You may, but are not required to, write doctests for this part.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import datetime


###################################################################################################
# Part 3, Question 1
###################################################################################################
def num_sections(course: tuple[str, str, set]) -> int:
    """Return the number of sections for the given course.

    Preconditions:
        - The input matches the format for a course described by the assignment handout.
    """
    return len(course[2])


def num_lecture_hours(section: tuple[str, str, tuple]) -> int:
    """Return the total number of lecture hours per week.

    Preconditions:
        - The input matches the format for a section described by the assignment handout.

    Hint: you can use ".hour" to access the hour attribute of a datetime.time value.
    """
    return sum([meeting[2].hour - meeting[1].hour for meeting in section[2]])


def sections_in_semester(schedule: dict[str, tuple[str, str, tuple]], semester: str) \
        -> set[tuple[str, str, tuple]]:
    """Return the set of all sections in schedule that are taken in semester.

    Courses that are taken in both semesters (i.e., 'Y') should always be included.

    Preconditions:
        - The input matches the format for a schedule described by the assignment handout.
        - semester in {'F', 'S'}
    """
    # return {(section for section in course[2] if section[1] == semester) for course in schedule.values()}
    return {section for section in schedule.values() if section[1] == semester or section[1] == 'Y'}


###################################################################################################
# Part 3, Question 2b
###################################################################################################
def times_conflict(m1: tuple[str, datetime.time, datetime.time],
                   m2: tuple[str, datetime.time, datetime.time]) -> bool:
    """Return whether the meeting times m1 and m2 conflict.

    Hint:
        - You can use comparison operators like < and == with datetime.time objects

    Preconditions:
        - m1 and m2 match the format for a meeting described by the assignment handout.
    """
    return m1[0] == m2[0] and m2[1].time < m1[2].time


def sections_conflict(s1: tuple[str, str, tuple], s2: tuple[str, str, tuple]) \
        -> bool:
    """Return whether the sections s1 and s2 conflict.

    Hint:
        - Use times_conflict

    Preconditions:
        - s1 and s2 match the format for a section described by the assignment handout.
    """
    same_term = s1[1] == s2[1]
    has_y_term = s1[1] == 'Y' or s2[1] == 'Y'

    has_conflict = any({times_conflict(m1, m2) for m1 in s1[2] for m2 in s2[2]})

    return (same_term or has_y_term) and not has_conflict


def is_valid(schedule: dict[str, tuple[str, str, tuple]]) -> bool:
    """Return whether the given schedule is valid.

    Hint:
        - Refer to the handout for a definition of a valid schedule

    Preconditions:
        - schedule matches the format for a schedule described by the assignment handout.
    """
    sections = list(schedule.values())
    return all({not sections_conflict(sections[i], sections[j]) for i in range(len(sections)) for j in range(i + 1, len(sections))})


def possible_schedules(c1: tuple[str, str, set], c2: tuple[str, str, set]) \
        -> list[dict[str, tuple[str, str, tuple]]]:
    """Return a list of all possible schedules of courses c1 and c2.

    Each returned schedule should contain exactly two key-value pairs, one with the course
    code and a section of c1, and the other with the course code and a section of c2.

    Invalid schedules are returned in this list.

    If a given course has no sections, then return an empty list.
    (This will happen "automatically" if you use a comprehension with an empty collection!)

    Preconditions:
        - c1 and c2 match the format for a course described by the assignment handout.
        - c1 != c2
    """

    return [{c1[0]: s1, c2[0]: s2} for s1 in c1[2] for s2 in c2[2]]


def valid_schedules(c1: tuple[str, str, set],
                    c2: tuple[str, str, set]) \
        -> list[dict[str, tuple[str, str, tuple]]]:
    """Return a list of all VALID schedules of courses c1 and c2.

    Each returned schedule should contain exactly two key-value pairs, one with the course
    code and a section of c1, and the other with the course code and a section of c2.

    Invalid schedules are NOT returned in this list.

    Hint:
        - Use is_valid
        - Use possible_schedules

    Preconditions:
        - c1 and c2 match the format for a course described by the assignment handout.
        - c1 != c2
    """
    return [s for s in possible_schedules(c1, c2) if is_valid(s)]


def possible_five_course_schedules(c1: tuple[str, str, set],
                                   c2: tuple[str, str, set],
                                   c3: tuple[str, str, set],
                                   c4: tuple[str, str, set],
                                   c5: tuple[str, str, set]) -> list[dict[str, tuple]]:
    """Return a list of every possible schedule that contains all given courses.

    This is analogous to possible_schedules, except now there are 5 courses instead of 2.

    If a given course has no sections, then return an empty list.
    (This will happen "automatically" if you use a comprehension with an empty collection!)

    Preconditions:
        - all given courses match the format for a course described by the assignment handout.
        - c1 != c2 and c1 != c3 and c1 != c4 and c1 != c5
        - c2 != c3 and c2 != c4 and c2 != c5
        - c3 != c4 and c3 != c5
        - c4 != c5

    HINT: you'll want a comprehension with 5 different variables. You can split up each
    "for ... in ..." across multiple lines to help make your code more readable.
    """
    return [{c1[0]: s1, c2[0]: s2, c3[0]: s3, c4[0]: s4, c5[0]: s5} 
            for s1 in c1[2] 
            for s2 in c2[2]
            for s3 in c3[2]
            for s4 in c4[2]
            for s5 in c5[2]
            ]

def valid_five_course_schedules(c1: tuple[str, str, set],
                                c2: tuple[str, str, set],
                                c3: tuple[str, str, set],
                                c4: tuple[str, str, set],
                                c5: tuple[str, str, set]) -> list[dict[str, tuple]]:
    """Return a list of every valid schedule that contains all given courses.

    This is analogous to valid_schedules, except now there are 5 courses instead of 2.

    Hint:
        - Use is_valid
        - Use possible_five_course_schedules

    Preconditions:
        - all given courses match the format for a course described by the assignment handout.
        - c1 != c2 and c1 != c3 and c1 != c4 and c1 != c5
        - c2 != c3 and c2 != c4 and c2 != c5
        - c3 != c4 and c3 != c5
        - c4 != c5
    """
    return [s for s in possible_five_course_schedules(c1, c2, c3, c4, c5) if is_valid(s)]


###################################################################################################
# Part 3, Question 3b
###################################################################################################
def is_section_compatible(schedule: dict[str, tuple[str, str, tuple]],
                          section: tuple[str, str, tuple]) -> bool:
    """Return whether the given section is compatible with the given schedule.

    Hint:
        - Refer to the handout for a definition of compatibility
        - Use sections_conflict
        - You can get a collection of only the values of a dict by using dict.values

    Preconditions:
        - section matches the format for a section described by the assignment handout.
        - schedule matches the format for a schedule described by the assignment handout.
    """
    return all({not sections_conflict(s, section) for s in schedule.values()})

def is_course_compatible(schedule: dict[str, tuple[str, str, tuple]],
                         course: tuple[str, str, set]) -> bool:
    """Return whether the given course is compatible with the given schedule.

    Hint:
        - Refer to the handout for a definition of compatibility
        - Use is_section_compatible

    Preconditions:
        - course matches the format for a course described by the assignment handout.
        - schedule matches the format for a schedule described by the assignment handout.
        - course[0] not in schedule
    """
    return any({is_section_compatible(schedule, s) for s in course[2]})


def compatible_sections(schedule: dict[str, tuple[str, str, tuple]],
                        course: tuple[str, str, set]) -> set[tuple[str, str, tuple]]:
    """Return the set of sections of the given course that are compatible with the given schedule.

    Hint:
        - Refer to the handout for a definition of compatibility
        - Use is_section_compatible

    Preconditions:
        - course matches the format for a course described by the assignment handout.
        - schedule matches the format for a schedule described by the assignment handout.
        - course[0] not in schedule
    """
    return {s for s in course if is_section_compatible(schedule, s)}


if __name__ == '__main__':
    # import python_ta
    # import python_ta.contracts
    # python_ta.contracts.DEBUG_CONTRACTS = False
    # python_ta.contracts.check_all_contracts()

    # import doctest
    # doctest.testmod()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # IMPORTANT: Leave this code uncommented when you submit your files.
    # python_ta.check_all(config={
    #     'extra-imports': ['datetime', 'python_ta.contracts'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'R1729']
    # })


    # import datetime
    # These are meeting times
    mon_9to11 = ('Monday', datetime.time(9), datetime.time(11))
    tues_9to11 = ('Tuesday', datetime.time(9), datetime.time(11))
    wed_9to11 = ('Wednesday', datetime.time(9), datetime.time(11))
    mon_1to3 = ('Monday', datetime.time(13), datetime.time(15))
    tues_1to3 = ('Tuesday', datetime.time(13), datetime.time(15))
    wed_1to3 = ('Wednesday', datetime.time(13), datetime.time(15))
    # These are sections
    csc110_lec0101 = ('LEC0101', 'F', (mon_9to11, tues_9to11, wed_9to11))
    csc110_lec0201 = ('LEC0101', 'F', (mon_1to3, tues_1to3, wed_1to3))
    # This is a course
    csc110 = ('CSC110', 'Foundations of Computer Science I',
              {csc110_lec0101, csc110_lec0201})
    
    csc108 = ('CSC108', 'Introduction to Computer Science I',
              {csc110_lec0101, csc110_lec0201})

    schedule = {'CSC110': csc110_lec0101}

    # print(sections_in_semester(schedule, 'F'))
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(possible_schedules(csc110, csc108))
