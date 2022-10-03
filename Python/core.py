import os
#import mysql.connector
import database
import game_functions
import helper

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

def decision():
    print("1. Steal")
    print("2. Escape")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break


    return userInput

def money_heist():
    return

def escape(airport_coordinates, max_flight_distance, player):
    os.system("cls")
    print("Possible airports:")
    
    airport_coordinates.extend(database.get_coordinates())
    possible_flights_index = helper.get_possible_flights(max_flight_distance, player[2], airport_coordinates)
    helper.print_possible_flights(possible_flights_index, airport_coordinates)
    
    return

def run_game(airport_data, player):
    os.system("cls")

    player = [""]
    player[0] = name 
    
    airport_coordinates = []
    max_flight_distance = 1000

    player.append("EFHK")
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            print("You are at", airport_data[i]["name"])
            player.append(airport_data[i]["deg"])
            break

    print("Coordinates:",player[2])
    input("Enter")
        
    
    
    print("Budget: ", budget, "€")
    print("CO2: ", co2, "kg")

    userSelection = decision()
    if userSelection == "1":
        money_heist()
    elif userSelection == "2":
        escape(airport_coordinates, max_flight_distance, player)

    input("Press Enter to continue...")



    return



#MAIN
budget  = 1000000
co2     = 100000
player  = [""]

airport_data = database.get_datalist()

os.system("cls")
name = input("Input name: ")
os.system("cls")


while True:
    userInput = print_mainmenu() #Print the main menu
    print(userInput)

    if userInput == "1":
        run_game(airport_data, player)
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
