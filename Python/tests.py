import mysql.connector
from math import sin, cos, sqrt, atan2, radians

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='eu_flight_game',
         user='root',
         password='root',
         autocommit=True
         )
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

def get_min_max_distance(airport_list):
    my_minimum = 1000000000
    my_maximum = -1000000000
    for i in range(len(airport_list)):
        print(i)
        for j in range(i + 1, len(airport_list)):
            if get_distances(airport_list[i], airport_list[j]) > my_maximum:
                my_maximum = get_distances(airport_list[i], airport_list[j])
            if get_distances(airport_list[i], airport_list[j]) < my_minimum:
                my_minimum = get_distances(airport_list[i], airport_list[j])

    return (my_maximum, my_minimum)

sql1 = "select latitude_deg, longitude_deg from eu_airports"

airport_list = []

cursor = connection.cursor()
cursor.execute(sql1)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        airport_list.append(row)

get_min_max_distance(airport_list)
print(airport_list)
