"""
Question (6 marks)

Implement the function 'count_distinct' according to the docstring provided.

You may use the Stack and Queue classes provided in module 'adts' to
create temporary Stack and/or Queue objects. These are the same Stack and
Queue classes you have seen before.

You must NOT create any other compound objects (lists, dictionaries, sets,
etc.)

You may create variables to store individual elements (counters, items that
have been popped or dequeued, etc.)

You may add doctest examples if desired.

Save your solution in a file called Q3_solution.py and hand it in on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from adts import Stack, Queue


def count_distinct(s: Stack) -> int:
    """Return the number of distinct items in the Stack s.

    Stack s will contain the same elements in the same order before and after
    count_distinct is called.

    Two items a and b are considered distinct if a != b.

    Preconditions:
    - The items in s can be compared using ==, !=, <, >, etc.
    - s is either sorted in non-decreasing or non-increasing order

    >>> s = Stack()
    >>> s.push(5)
    >>> s.push(5)
    >>> s.push(5)
    >>> s.push(2)
    >>> s.push(1)
    >>> s.push(0)
    >>> s.push(0)
    >>> count_distinct(s)
    4
    >>> s.pop()
    0
    >>> s.pop()
    0
    >>> s.pop()
    1
    >>> s.pop()
    2
    >>> s.pop()
    5
    >>> s.pop()
    5
    >>> s.pop()
    5
    >>> s.is_empty()
    True
    """
    temp = Stack()
    count = 0

    # get the first item
    if not s.is_empty():
        a = s.pop()
        temp.push(a)
        count += 1

    while not s.is_empty():
        b = s.pop()
        # if a is not the same as the next item
        if a != b:
            count += 1
        temp.push(b)
        # update a to the next item
        a = b

    # move everything back
    while not temp.is_empty():
        s.push(temp.pop())

    return count
