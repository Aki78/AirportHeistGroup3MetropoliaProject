# data should be a dictionary with all the info
airports = {}
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )


# possibly make double these functions for plural
def get_aiport_info():
    pass

# def get_weather():
#    pass
