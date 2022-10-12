import random
import database
import gfuncs
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

    a = (sin(lat_distance / 2)) ** 2 + cos(lat_and_long[0] / 180 * 3.14) * cos(lat_and_long[2] / 180 * 3.14) * (sin(long_distance / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

def get_possible_flights(max_flight_distance, player_coordinates, deg_list):
    possible_airport_name_list = []
    
    for new_coordinates in deg_list:
        if get_distances(player_coordinates, new_coordinates) <= max_flight_distance and get_distances(player_coordinates, new_coordinates) != 0:
            possible_airport_name_list.append(database.get_airport_name(new_coordinates))

    return possible_airport_name_list

def chooose_destination(airport_data):
    random.seed()

    d_code = ''
    d_country = ''

    destination_list = ["GCFV", "LPFR", "LMML"]

    d_code = random.choice(destination_list)
    
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == d_code:
            d_country = airport_data[i]["country"]

    return d_code, d_country

def print_possible_flights(airport_data, name, coordinates):
    selection = 1

    for i in name:
        print(selection, "- ", i)

        for j in range(len(airport_data)):
            if airport_data[j]["name"] == i:
                print(j, " - Country: ",airport_data[j]["country"])
        
        selection += 1
      
    return selection

def print_flight_details(name_list, selection, player_coordinates):
    airport_geo_data = database.get_geo_airport_info(name_list[selection])
    print("Airport name :", airport_geo_data[0])
    print("City         :", airport_geo_data[1])
    print("Country      :", airport_geo_data[2])
    print("ICAO code    :", airport_geo_data[3])

    price               = gfuncs.get_ticket_price(get_distances(player_coordinates, (airport_geo_data[4], airport_geo_data[5])))
    stamina_consumption = gfuncs.get_stamina_consumptions(get_distances(player_coordinates, (airport_geo_data[4], airport_geo_data[5])))
    new_coordinates     = database.get_new_coordinates(airport_geo_data[3])

    print("Price        :", price, "€")
    print("Stamina cost :", stamina_consumption)

    return price, stamina_consumption, airport_geo_data[3], new_coordinates

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
