"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Mario Badr, Tom Fairgrieve, Amanjit Kainth, Kaveh Mahdaviani,
Sadia Sharmin, and Joseph Jay Williams
"""
from typing import TextIO
from flight_constants import AirportDict, RouteDict

import flight_example_data


################################################################################
# Constants
################################################################################
INDEX_AIRPORTS_IATA = 0
INDEX_AIRPORTS_NAME = 1
INDEX_AIRPORTS_CITY = 2
INDEX_AIRPORTS_COUNTRY = 3
INDEX_AIRPORTS_LATITUDE = 4
INDEX_AIRPORTS_LONGITUDE = 5
INDEX_AIRPORTS_TZ = 6


################################################################################
# Part 1 - Reading the data
################################################################################
def read_airports(airports_data: TextIO) -> AirportDict:
    """Return a dictionary based on the data in airports_data. The dictionary
    maps IATA airport codes to another dictionary containing information about
    that airport.

    The dictionary containing information about an airport maps string keys
    that identify the information to the respective data found in airports_data.
    The keys are: Name, City, Country, Latitude, Longitude, and Tz.

    Precondition:
        - Every IATA airport code in the data is unique
        - The data in airports_data is formatted correctly

    >>> example_airport_file = flight_example_data.create_airport_file()
    >>> actual = read_airports(example_airport_file)
    >>> actual == flight_example_data.create_example_airports()
    True
    """
    airports = {}
    for line in airports_data:
        data = line.replace('"', '').strip().split(',')

        iata = data[INDEX_AIRPORTS_IATA]

        airport = {
            'Name': data[INDEX_AIRPORTS_NAME],
            'City': data[INDEX_AIRPORTS_CITY],
            'Country': data[INDEX_AIRPORTS_COUNTRY],
            'Latitude': data[INDEX_AIRPORTS_LATITUDE],
            'Longitude': data[INDEX_AIRPORTS_LONGITUDE],
            'Tz': data[INDEX_AIRPORTS_TZ]
        }
        
        airports[iata] = airport
    # print(airports)
    return airports

def read_routes(routes_data: TextIO, airports: AirportDict) -> RouteDict:
    """Return the flight routes from routes_data.

    Do not include the routes with source or destination airport codes that are
    not in airports.

    Preconditions:
        - The data in routes_data is formatted correctly

    >>> example_routes_file = flight_example_data.create_route_file()
    >>> example_airports = flight_example_data.create_example_airports()
    >>> actual = read_routes(example_routes_file, example_airports)
    >>> actual == flight_example_data.create_example_routes()
    True
    """
    routes = {}
    line = routes_data.readline()
    while line != "":
        src = line.strip().split(": ")[1]
        
        dst_dict = {}

        routes_data.readline() # BEGIN

        line = routes_data.readline()
        while not line.startswith("DESTINATIONS END"):
            lst = line.strip().split()

            dst = lst[0]
            planes = lst[1:]

            if dst in airports:
                dst_dict[dst] = planes
            
            line = routes_data.readline()

        if src in airports and dst_dict:
            routes[src] = dst_dict
        
        line = routes_data.readline()

    return routes


if __name__ == '__main__':
    # Enable type contract checking for the functions in this file
    import sys
    sys.path.insert(0, 'pyta')    
    import pyta.python_ta.contracts
    pyta.python_ta.contracts.check_all_contracts()  

    # Check the correctness of the doctest examples
    import doctest
    doctest.testmod()

    # Check style with python_ta    
    import pyta.python_ta
    import json
    json_config = json.loads(open('pyta/a3_pyta.json').read())
    pyta.python_ta.check_all(config=json_config)    

    # Uncomment the lines below to open the files and call your functions above
    #airport_file = open('data/airports.csv', encoding='utf8')
    #airports = read_airports(airport_file)
    #airport_file.close()
    #routes_file = open('data/routes.dat', encoding='utf8')
    #routes = read_routes(routes_file, airports)
    #routes_file.close()

    