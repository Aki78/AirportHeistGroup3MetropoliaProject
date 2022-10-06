import os
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'eu_flight_game',
    user = 'root',
    password = 'root',
    autocommit=True
)

def print_mainmenu():
    userInput = 0
    
    while True:
        os.system("cls")

        print("Welcome to flight game")
        print("")
        print("Hello, "+ str(name) + "!")

        print("1. Start")
        print("2. Settings")
        print("3. Instructions")
        print("4. Credits")
        print("5. Exit")

        userInput = input("Input: ")

        if userInput == "" or int(userInput) < 1 or int(userInput) > 5:
            print("Invalid input")
            input("Press Enter to continue...")
        else:
            return str(userInput)

def print_settings():
    os.system("cls")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
    return

def print_instructions():
    os.system("cls")
    print("This is the instructions")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    input("Press Enter to continue...")
    return

def print_credits():
    os.system("cls")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
    return

def run_game():
    os.system("cls")

    sql = "select name, municipality, ident, latitude_deg, longitude_deg from eu_airports "
    sql += "where ident = 'EDDB'"
    
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print("You are at", result[0][0])
    print("Reachable airports:")

    print_reachable_airports(result[0][3], result[0][4]) #Pass lat and long to func

    input("Press Enter to continue...")
    return

def print_reachable_airports():
    
    return

budget = 1000000
co2 = 100000
player = [""]

os.system("cls")
name = input("Input name: ")
os.system("cls")


while True:
    userInput = print_mainmenu() #Print the main menu
    print(userInput)

    if userInput == "1":
        run_game()
    elif userInput == "2":
        print_settings()
    elif userInput == "3":
        print_instructions()
    elif userInput == "4":
        print_credits()
    elif userInput == "5":
        os.system("cls")
        input("Press Enter to exit...")
        break       
