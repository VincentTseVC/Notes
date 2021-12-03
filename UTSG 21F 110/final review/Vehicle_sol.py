"""
QUESTION 2: Object Oriented Programming

8 marks, ~15 minutes

(a) Write a series of classes that satisfy the following specification.

A parking garage has an address (an arbitrary string), and zero or more vehicle
parked in it. Because of local laws a parking garage can host at most 1000
parking spots. If a vehicle tries to enter the parking garage that does not have
enough parking spots left, a NoParkingAvailableError is raised.

A vehicle can either be a truck or a car. Trucks are longer than cars and have
to park at an angle, taking up two parking spots at a time. Cars can park
normally and take up one parking spot in the parking garage.

Both trucks and cars have a make, colour and year in which they are built.

TODO: Write your code below here.

You may import any type of from "typing" for type contracts. No other import is
allowed.

Documentation are not required for the marking of this question; however, it may
help the TAs understand your code better.
"""
from typing import List

class NoParkingAvailableError(Exception):
    pass

class Vehicle:

    make: str
    colour: str
    year: int

    def __init__(self, make: str, colour: str, year: int) -> None:
        self.make = make
        self.colour = colour
        self.year = year
    
    def spot_required(self) -> float:
        raise NotImplementedError

class Car(Vehicle):

    def spot_required(self) -> float:
        return 1.0


class Truck(Vehicle):

    def spot_required(self) -> float:
        return 2.0

class Garage:
    address: str
    vehicles: List[Vehicle]
    spots: int

    def __init__(self, address: str, spots: int) -> None:
        self.address = address
        self.spots = spots
        self.vehicles = []
    

    def park(self, vehicle: Vehicle) -> None:
        spot = vehicle.spot_required()
        # not enough spots to part this vehicle
        if self.spots - spot < 0:
            raise NoParkingAvailableError
        else:
            self.vehicles.append(vehicle)
            self.spots -= spot





"""
(b) Write code in the __main__ block below to perform the following.

- Create a new parking garage.
- Write a loop and add 400 trucks and 199 cars to the parking garage.
- Ask the user for a year, make and colour of a car and instantiate a new 
  object with these attributes.
- Add the newly created car to the parking garage with the following 
  considerations: 
  - If this raises a NoParkingAvailableError, print "Sorry, No parking" without 
    crashing the program.
"""

if __name__ == "__main__":

    try:
        parking_lot = Garage("123 address", 1000)

        for i in range(400):
            parking_lot.park(Truck("Toyota", "White", 2021))
        
        for i in range(199):
            parking_lot.park(Car("Lexus", "Black", 2021))
        
        year = int(input("Please enter the year of the car: "))
        make = input("Please enter the make of the car: ")
        colour = input("Please enter the colour of the car: ")

        parking_lot.park(Car(make, colour, year))
    except NoParkingAvailableError:
        print("Sorry, No parking")

