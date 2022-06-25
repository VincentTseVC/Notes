"""Drivers for the simulation"""

from location import Location, manhattan_distance
from passenger import Passenger
from typing import Optional


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    id: A unique identifier for the driver.
    location: The current location of the driver.
    is_idle: True if the driver is idle and False otherwise.

    === Private Attributes ===
    _speed: The drivers speed.
    _destination: The destination of the driver. None if the driver has no destination
        and is idle.
    _passenger: The current passenger for the driver, or None if the driver is not
          currently driving a passenger.
    """

    id: str
    location: Location
    is_idle: bool
    _speed: int
    _destination: Optional[Location]
    _passenger: Optional[Passenger]

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a Driver.

        """
        # TODO
        self.id = identifier
        self.location = location
        self._speed = speed
        self.is_idle = True
        self._destination = None
        self._passenger = None

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'Driver[{self.id}]'

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        # TODO
        return self.id == other.id and \
               self.location == other.location and \
               self._speed == other._speed and \
               self.is_idle == other.is_idle and \
               self._destination == other._destination and \
               self._passenger == other._passenger

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        # TODO
        distance = manhattan_distance(self.location, destination)
        return int(round(distance / self._speed))

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        # TODO
        if not self.is_idle:
            raise Exception
        
        self._destination = location
        self.is_idle = False
        return self.get_travel_time(location)

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        """
        # TODO
        self.location = self._destination
        self.is_idle = True
        self._destination = None

    def start_trip(self, passenger: Passenger) -> int:
        """Start a ride and return the time the ride will take.

        """
        # TODO
        self._passenger = passenger
        self._destination = passenger.destination
        self.is_idle = False
        return self.get_travel_time(self._destination)

    def end_trip(self) -> None:
        """End the current ride, and arrive at the passenger's destination.

        Precondition: The driver has a passenger.
        Precondition: self.destination is not None.

        """
        # TODO
        self.location = self._destination
        self.is_idle = True
        self._destination = None
        self._passenger = None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        config={'extra-imports': ['location', 'passenger']})
