"""
QUESTION 3: ADT

6 marks, ~15 minutes

In this question, we want to implement an ADT called QStack, which stores a
collection of integers and supports the following operations.

- push():       push a new item onto the QStack
- pop():        pop and return the newest item from the QStack
- dequeue():    remove and return the oldest item from the QStack

That's right: we want QStack to behave like both Stack and Queue. Furthermore,
ALL above operations must have O(1) time complexity, i.e., constant time.

You are required to use a Python dictionary (_items) to implement this class.

You may assume that Python dictionary's lookup and insert operations both have
O(1) complexity, i.e., they take constant time.

TODO: Complete the implementation of the QStack below.

You may add new instance variables or helper methods if necessary, but you're
NOT allowed to modify the type contract of any of the given methods and
attributes. You're NOT allowed to add any import.

Documentation are not required for the marking of this question; however, it may
help the TAs understand your code better.
"""

from typing import Dict


class QStack:
    """
    An ADT that supports both Stack and Queue operations.
    """

    _items: Dict[int, int]
    _top: int
    _bot: int

    def __init__(self) -> None:
        """
        Initialize an empty QStack
        """
        self._items = dict()
        self._top = 0
        self._bot = 0

    def push(self, item: int) -> None:
        """
        push a new item onto the QStack
        """
        # (first time)
        if self._bot == 0:
            self._bot += 1

        self._top += 1
        self._items[self._top] = item

    def pop(self):
        """
        pop and return the newest item in the QStack
        return None if the QStack is empty
        """
        if self.is_empty():
            return None

        item = self._items[self._top]
        self._top -= 1
        return item

    def dequeue(self):
        """
        remove and return the oldest item in the QStack
        return None if the QStack is empty
        """
        if self.is_empty():
            return None
        
        item = self._items[self._bot]
        self._bot += 1
        return item

    def is_empty(self):
        return self._bot > self._top or self._bot == 0

'''
    {
        1: "A",   
        2: "B",   top
        3: "C",   bot
        4: "D",   
        5: "E"


     }
'''
