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
from pyta.python_ta import reset_linter
from flight_reader import INDEX_AIRPORTS_TZ
from typing import Dict, List, Tuple
from flight_constants import AirportDict, RouteDict, OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################
def is_direct_flight(routes: RouteDict, iata_src: str, iata_dst: str) -> bool:
    """aaa
    """

    if iata_src not in routes:
        return False
    
    if iata_dst not in routes[iata_src]:
        return False
    
    return True

def is_valid_flight_sequence(routes: RouteDict, iata_list: List[str]) -> bool:
    """aa
    """
    if len(iata_list) < 2:
        return False

    for i in range(len(iata_list) - 1):
        src = iata_list[i]
        dst = iata_list[i + 1]
        if not is_direct_flight(src, dst, routes):
            return False

    return True

def summarize_by_timezone(airports: AirportDict) -> Dict[str, int]:
    """aaa
    """
    timezone_count = {}
    
    for airport in airports:
        timezone = airport[INDEX_AIRPORTS_TZ]

        if timezone != OPENFLIGHTS_NULL_VALUE:
            if timezone in timezone_count:
                timezone_count[timezone] += 1
            else:
                timezone_count[timezone] = 1

    return timezone_count


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################
def find_reachable_destinations(routes: RouteDict, source: str, num: int) -> \
        List[str]:
    """Return the list of IATA airport codes that are reachable from source by
    taking at most num direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in lexicographical order (use the
    list.sort() method on a list of strings to achieve this).

    Preconditions:
        - num >= 1
        - (source in routes) is True

    >>> example_routes = flight_example_data.create_example_routes()
    >>> find_reachable_destinations(example_routes, 'GFN', 1)
    ['TRO']
    >>> find_reachable_destinations(example_routes, 'GFN', 2)
    ['GFN', 'SYD', 'TRO']
    """

    reachable_list = []

    stops = [source]

    for _ in range(num):
        new_stops = []
        for src in stops:
            for dst in routes[src]:
                if dst not in reachable_list:
                    new_stops.append(dst)
                    reachable_list.append(dst)
        stops = new_stops
    
    reachable_list.sort()
    return reachable_list


def decommission_plane(routes: RouteDict, plane: str) -> List[Tuple[str, str]]:
    """Update routes by removing plane from all source-destination routes that
    use plane. Do not remove the source-destination pair, only the plane.

    In addition, return a sorted list of two-element tuples where the first
    index is source and the second index is destination (use the list.sort()
    method on a list of tuples to achieve this). The list includes *all* routes
    that that have no planes that can be used.

    >>> example_routes = flight_example_data.create_example_routes()
    >>> decommission_plane(example_routes, 'DH4')
    []
    >>> example_routes['TRO']['SYD']
    ['SF3']
    >>> example_routes = flight_example_data.create_example_routes()
    >>> decommission_plane(example_routes, 'SF3')
    [('GFN', 'TRO'), ('JCK', 'RCM'), ('RCM', 'JCK'), ('TRO', 'GFN')]
    >>> example_routes['TRO']['SYD']
    ['DH4']
    """
    pairs = []
    for src in routes:
        for dst in routes[src]:
            planes = routes[src][dst]
            if plane in planes:
                planes.remove(plane)

            if len(planes) == 0:
                pairs.append((src, dst))
    
    pairs.sort()
    return pairs



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
