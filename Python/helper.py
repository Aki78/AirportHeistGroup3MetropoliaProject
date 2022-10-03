from math import sin, cos, sqrt, atan2, degrees

def feet_to_meters(feet):
    meters = 0.3048 * feet
    return meters

def meters_to_km(meters):
    kilometers = 1000 * meters
    return(kilometers)

def get_distances(deg1, deg2):
    R = 6371.0

    lat_and_long = []

    lat_and_long.append(deg1[0])
    lat_and_long.append(deg1[1])


    lat_and_long.append(deg2[0])
    lat_and_long.append(deg2[1])

    lat_distance = (lat_and_long[2] - lat_and_long[0]) / 180 * 3.14
    long_distance = (lat_and_long[3] - lat_and_long[1]) / 180 * 3.14



    a = (sin(lat_distance / 2)) ** 2 + cos(lat_and_long[0] / 180 * 3.14) * cos(lat_and_long[2] / 180 * 3.14) * (
        sin(long_distance / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c


    return distance

def get_possible_flights(max_flight_distance, player_position, deg_list):
    my_index = []
    for i in range(deg_list):
        if get_distances(player_position, i) < max_flight_distance:
            my_index.append(i)
    return my_index



def deg_to_xy(deg):
    y = 111 * deg[1]
    x = 0.63 * 111 * deg[0]
    return(x, y)

def get_min_max_distance(airport_list):
    my_minimum = 1000000000
    my_maximum = -1000000000
    for i in range(len(airport_list)):
        for j in range(i + 1, len(airport_list)):
            if get_distances(airport_list[i], airport_list[j]) > my_maximum:
                my_maximum = get_distances(airport_list[i], airport_list[j])
            if get_distances(airport_list[i], airport_list[j]) < my_minimum:
                my_minimum = get_distances(airport_list[i], airport_list[j])

    return (my_maximum, my_minimum)


