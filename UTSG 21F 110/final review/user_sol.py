"""
Question [12 marks]

In this question, you will complete a program that allows a user to create
checklists with items to be done and record when items are completed.
- A checklist has a name (str) and a list of checklist items.
- A checklist item has a description (str), a deadline (date), and
  the name of the user who completed the item.
- A user has a name (str) and the total number items they have completed (int).
You will need to write one class for each of these entities.

In the __main__ block below is an example of how we want to use these
classes. Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.  Any unspecified
behaviour is up to you -- it will not be tested.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool, and date may be public, but all other attributes
must be private. You may add imports from the typing module, but do NOT add any
other imports.

Your code will be marked for correctness and design, as well as for having
class docstrings that follow the Class Design Recipe. Docstrings for your
methods are NOT required.

Save your solution in a file called Q5_solution.py and submit it on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from __future__ import annotations
from datetime import date
from typing import List, Dict


# TODO: Define the 3 necessary classes here.
class User:
    """
    do it yourself
    """
    name: str
    total_items_checked: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.total_items_checked = 0


class Item:
    """
    do it yourself
    """
    description: str
    deadline: date
    user: str

    def __init__(self, description: str, deadline: date) -> None:
        self.description = description
        self.deadline = deadline
        self.user = ""


class Checklist:
    """
    do it yourself
    """
    name: str
    _items: Dict[str, Item]

    def __init__(self, name: str) -> None:
        self.name = name
        self._items = dict()

    def create_item(self, description: str, deadline: date) -> None:
        self._items[description] = Item(description, deadline)

    def mark_item_complete(self, description: str, user: User) -> None:
        if description in self._items:
            self._items[description].user = user.name
            user.total_items_checked += 1

    def has_item(self, description: str) -> bool:
        return description in self._items

    def __str__(self) -> str:
        result = self.name
        for item in self._items.values():
            if item.user == "":
                result += f'\n[-] {item.description} {item.deadline}'
            else:
                result += f'\n[x] {item.description} {item.deadline}' \
                          f', completed by {item.user}'
        return result


if __name__ == "__main__":
    # Instantiate three users
    manila = User('Manila')
    sofija = User('Sofija')
    felix = User('Felix')

    # Instantiate a checklist
    manilas_checklist = Checklist('Planner for M')

    # Manila adds some items to the checklist, the first one she adds is Math
    # Homework due on March 1st.
    manilas_checklist.create_item('Math Homework', date(2021, 3, 1))
    manilas_checklist.create_item('pick up milk', date(2021, 2, 25))
    manilas_checklist.create_item('CSC148 A1', date(2021, 3, 2))

    # Manila finishes her CSC148 assignment and marks it complete
    manilas_checklist.mark_item_complete('CSC148 A1', manila)

    # Sofija attempts to check off an item as complete that isn't in
    # manilas_checklist.  This does nothing.
    manilas_checklist.mark_item_complete('MAT157 Review', sofija)

    # Sofija picks up milk for Manila.
    manilas_checklist.mark_item_complete('pick up milk', sofija)

    print(manilas_checklist)
    # The output is below. Notice that the order is based on the order they
    # were added to manilas_checklist.  Output:
    # Planner for M
    # [-] Math Homework (2021-03-01)
    # [x] pick up milk (2021-02-25), completed by Sofija
    # [x] CSC148 A1 (2021-03-02), completed by Manila

    # confirm the check list items are all present in the checklist
    for item_description in ['Math Homework', 'pick up milk', 'CSC148 A1']:
        assert manilas_checklist.has_item(item_description)

    # Felix completed no checklist items
    assert felix.total_items_checked == 0
    # Manila and Sofija each completed one checklist item
    assert manila.total_items_checked == 1
    assert sofija.total_items_checked == 1
