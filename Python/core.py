import os
import string
import database
import gfuncs
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

def decision(): #Input
    print("1. Steal")
    print("2. Escape")
    print("")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break


    return userInput

def print_player_position(airport_data, player):
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            print("You are at", airport_data[i]["name"])
            break
    return

def money_heist():
    return

def escape(airport_coordinates, max_flight_distance, player):
    os.system("cls")
    
    airport_coordinates         = []
    possible_flights_name       = []
    amount_of_possible_flights  = 0
    
    print("Possible airports:")
    
    airport_coordinates.extend(database.get_coordinates())
    
    possible_flights_name           = helper.get_possible_flights(max_flight_distance, player[2], airport_coordinates)  #Return name list of possible airports
    
    amount_of_possible_flights      = helper.print_possible_flights(possible_flights_name, airport_coordinates)         #Check amount of possible airports (for later use)
    
    price, stamina, new_icao_code   = player_airport_selection(possible_flights_name, airport_coordinates, player[2], amount_of_possible_flights)    #Player choose the airport and return the icao code of destination

    if new_icao_code is not None:
        return price, stamina, new_icao_code
    else:
        return 0, 0, None

def player_airport_selection(name_list, coordinates, player_coordinates, amount_of_possible_flights):
    userInput = "0"

    #Input airport decision (fix later)
    while True:
        userInput = input("Input: ").strip()

        if userInput == "" or type(int(userInput)) is not int:
            print("Invalid input")
        #elif 1 > int(userInput) or int(userInput) > amount_of_possible_flights + 1:
        #    print("Invalid input")
        else:
            selection = int(userInput) - 1
            break

    os.system("cls")
    price, stamina, icao_code = helper.print_flight_details(name_list, selection, player_coordinates)

    print("1. Travel")
    print("2. Stay")
    print("")

    #Input decision (also fix later)
    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break

    if int(userInput) == 1:
        return price, stamina, icao_code
    elif int(userInput) == 2:
        return 0, 0, None
    

def update_player(player, price, stamina, new_icao_code):
    player[1] = new_icao_code
    player[3] -= price
    player[4] -= stamina
    return player
 
def run_game(airport_data, player):
    os.system("cls")

    player = [""]
    player[0] = name 
    
    airport_coordinates = []
    max_flight_distance = 1000

    player.append("EFHK")

    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            player.append(airport_data[i]["deg"])
            break
    
    player.append(1000000)
    player.append(10000)
        
    while budget > 0 or stamina > 0:
        os.system("cls")
        print_player_position(airport_data, player)

        print("Budget   : ", player[3], "€")
        print("Stamina  : ", player[4])

        userSelection = decision()
        if userSelection == "1":
            money_heist()
        elif userSelection == "2":
            price, stamina, new_icao_code = escape(airport_coordinates, max_flight_distance, player)
            if new_icao_code is not None:
                player = update_player(player, price, stamina, new_icao_code)
                print(player)
                       
    

    input("Press Enter to continue...")

    return


#MAIN
budget  = 1000000
stamina = 100000
player  = [""]  #player = ['name', 'position_code', coordinates, budget, stamina]

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
