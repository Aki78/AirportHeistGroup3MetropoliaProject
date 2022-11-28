import helper
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='eu_flight_game',
    user='root',
    password='root',
    autocommit=True
)

data_list = []
sql = "select ident, latitude_deg, longitude_deg from eu_airports"
    
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        data_list.append( {"ident": row[0], "distance": helper.get_distances((60.3172, 24.963301), (row[1], row[2]))} )

new_list = sorted(data_list, key = lambda d: d['distance'], reverse = True)

print(new_list)