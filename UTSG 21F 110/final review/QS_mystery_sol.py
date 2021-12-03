"""
TEST 1 QUESTION 3
Abstract Data Types

STEP 1: Scroll past this reference code for Stack and Queue, which is needed
for the following question :)

"""


from typing import List, Optional, Any


###############################################################################
# Stack
###############################################################################

class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    === Private Attributes ===
    _items:
        The items stored in this stack. The end of the list represents
        the top of the stack.
    """

    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()


class EmptyStackError(Exception):
    """Exception raised when calling pop on an empty stack."""
    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'You called pop on an empty stack.'


###############################################################################
# Queue
###############################################################################

class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.

    === Private attributes ===
    _items: a list of the items in this queue
    """

    _items: List

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('hello')
        >>> q.is_empty()
        False
        """
        return self._items == []

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return the item at the front of this queue.

        Return None if this Queue is empty.
        (We illustrate a different mechanism for handling an erroneous case.)

        >>> q = Queue()
        >>> q.enqueue('hello')
        >>> q.enqueue('goodbye')
        >>> q.dequeue()
        'hello'
        """
        if self.is_empty():
            return None
        else:
            return self._items.pop(0)


"""

Whew! You're here!

4 marks
Here's a mystery function.
"""

'''
    ori =     1   5   4   2   3

    var1 =    5   1   2   4   3

    var2 =      

    var3 =    

    swap swap ....

'''


def miss_tree(var1):
    var2 = Queue()
    var3 = Queue()
    while not var1.is_empty():
        var2.enqueue(var1.dequeue())
        if not var1.is_empty():
            var3.enqueue(var1.dequeue())
    while not (var2.is_empty() or var3.is_empty()):
        var1.enqueue(var3.dequeue())
        var1.enqueue(var2.dequeue())


    if not var3.is_empty():
        var1.enqueue(var3.dequeue())
    elif not var2.is_empty():
        var1.enqueue(var2.dequeue())


"""
Rewrite the function below, making these changes:
    -- Give the function and all variables reasonable names.
    -- Write a type contract.
    -- Write a descriptive docstring that tells what it does.
    -- Write one helpful docstring example showing a test case.
    Do not change anything else about it. (That said, you may add comments.)

# TODO Copy the mystery function and make the required changes & documentation

"""

def swap(queue):
    """swap the items at even position with the item at odd positions in the queue.

    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(5)
    >>> q.enqueue(4)
    >>> q.enqueue(2)
    >>> q.enqueue(3)
    >>> swap(q)
    >>> q.dequeue()
    5
    >>> q.dequeue()
    1
    >>> q.dequeue()
    2
    >>> q.dequeue()
    4
    >>> q.dequeue()
    3
    """
    even = Queue() # items at even posotion
    odd = Queue() # items at odd popsition
    while not queue.is_empty():
        even.enqueue(queue.dequeue())
        if not queue.is_empty():
            odd.enqueue(queue.dequeue())
    while not (even.is_empty() or odd.is_empty()):
        queue.enqueue(odd.dequeue())
        queue.enqueue(even.dequeue())


    if not odd.is_empty():
        queue.enqueue(odd.dequeue())
    elif not even.is_empty():
        queue.enqueue(even.dequeue())



