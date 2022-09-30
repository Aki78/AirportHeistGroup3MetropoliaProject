def feet_to_meters(feet):
    meters = 0.3048 * feet
    return meters

def meters_to_km():
    pass

def get_distances(deg1, deg2):
    from math import sin, cos, sqrt, atan2, degrees
    R = 6371.0

    lat_and_long = []
    print(f"The latitude for ICAO1 is {deg1[0]} and the location is {deg1[1]}")
    lat_and_long.append(deg1[0])
    lat_and_long.append(deg1[1])

    print(f"The latitude for ICAO1 is {deg2[0]} and the longitude is {deg2[1]}")
    lat_and_long.append(deg2[0])
    lat_and_long.append(deg2[1])

    lat_distance = (lat_and_long[2] - lat_and_long[0]) / 180 * 3.14
    long_distance = (lat_and_long[3] - lat_and_long[1]) / 180 * 3.14

    print(f" the difference in lat is {lat_distance} and the difference in long is {long_distance}.")

    a = (sin(lat_distance / 2)) ** 2 + cos(lat_and_long[0] / 180 * 3.14) * cos(lat_and_long[2] / 180 * 3.14) * (
        sin(long_distance / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    print(f" The distance between the two airports is {distance}km.")
    return(distance)
    pass

def get_possible_flights():
    pass

