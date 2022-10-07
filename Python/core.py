import os
import database
import gfuncs
import helper
import random

def print_mainmenu():
    userInput = 0

    while True:
        os.system("cls")

        print("Welcome to flight game")
        print("")
        print("Hello, " + str(name) + "!")

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
    print("1 - You are limited by budget and stamina.")
    print("2 - You have to by tickets to travel.")
    print("3 - In order to acquire money, you have to steal.")
    print("4 - You can get caught by the interpol, but you are informed about the odds.")
    print("5 - You can see in which possible cities the interpol will be, but not where they will go next.")
    print("6 - You are restricted to airports with-in a certain distance.")
    print("7 - You will lose if you go under stamina or budget.")


    input("Press Enter to continue...")
    return


def print_credits():
    os.system("cls")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
    return


def decisions(): #Input
    print("1. Heist")
    print("2. Escape")
    print("")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break

    print(userInput)
    return userInput


def print_player_position(airport_data, player):
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            print("You are at", airport_data[i]["name"])
            break
    return


def money_heist(player, rate_up, rate_down, attempt):
    os.system("cls")
    if attempt > 0:
        print("Your are about to steal more money")
        steal_rate = round(gfuncs.theft_success_rate() * 100) / 100

        print("Successful stealing rate: ", steal_rate * 100, "%")
        print("1. Steal")
        print("2. Later")
        print("")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break

    if userInput == "1":
        os.system("cls")
        stolen_money = gfuncs.theft_success_earnings_gauss()
        print("Got", stolen_money, "€")

        true_rate = random.uniform(rate_down, rate_up)
        # print("true rate", true_rate)
        if true_rate <= steal_rate:
            print("Steal successful")
            player[3] += stolen_money
            input("Press Enter to continue")
        else:
            print("You got caught")
            print("You lost")
            input("Press Enter to continue")

            return player, True, attempt

        if userInput == "1":
            os.system("clr")
            stolen_money = gfuncs.theft_success_earnings_gauss()
            print("Got", stolen_money, "€")

            true_rate = random.random()
            #print("true rate", true_rate)
            if true_rate <= steal_rate:
                print("Steal successful")
                player[3] += stolen_money
                input("Press Enter to continue")
            else:
                print("You got caught")
                print("You lost")
                input("Press Enter to continue")
                return player, True, attempt
    elif userInput == "2":
        attempt -= 1
    if attempt == 0:
        print("You got caught!")
        got_caught = True
        return player, got_caught, attempt
    return player, False, attempt


def escape(airport_coordinates, max_flight_distance, player,attempt):
    attempt = 5
    os.system("cls")

    airport_coordinates = []
    possible_flights_name = []
    amount_of_possible_flights = 0

    print("Possible airports:")

    airport_coordinates.extend(database.get_coordinates())

    # Return name list of possible airports
    possible_flights_name = helper.get_possible_flights(max_flight_distance, player[2], airport_coordinates)

    # Check amount of possible airports (for later use)
    amount_of_possible_flights = helper.print_possible_flights(possible_flights_name, airport_coordinates)

    # Player choose the airport and return the icao code of destination
    price, stamina, new_icao_code, new_coordinates = player_airport_selection(possible_flights_name,
                                                                              airport_coordinates, player[2],
                                                                              amount_of_possible_flights)

    if new_icao_code is not None:
        #print("Waiting for new code 1", new_icao_code)
        return price, stamina, new_icao_code, new_coordinates, attempt
    else:
        return 0, 0, None, (0, 0), 0


def player_airport_selection(name_list, coordinates, player_coordinates, amount_of_possible_flights):
    userInput = "0"

    # Input airport decision (fix later)
    while True:
        userInput = input("Input: ").strip()

        if userInput == "" or type(int(userInput)) is not int:
            print("Invalid input")
        # elif 1 > int(userInput) or int(userInput) > amount_of_possible_flights + 1:
        #    print("Invalid input")
        else:
            selection = int(userInput) - 1
            break

    os.system("cls")
    price, stamina, icao_code, new_coordinates = helper.print_flight_details(name_list, selection, player_coordinates)

    print("1. Travel")
    print("2. Stay")
    print("")

    # Input decision (also fix later)
    while True:
        userInput = input("Input: ")

        if str(userInput) != "1" and str(userInput) != "2":
            print("Invalid input")
        else:
            break

    if int(userInput) == 1:
        #print("Waiting for new code 2", icao_code)
        return price, stamina, icao_code, new_coordinates
    elif int(userInput) == 2:
        return 0, 0, None, (0, 0)


def update_player(player, price, stamina, new_icao_code, new_coordinates):
    player[1] = new_icao_code
    player[2] = new_coordinates
    player[3] -= price
    player[4] -= stamina
    return player


def run_game(airport_data, player):
    os.system("cls")

    player = [""]
    player[0] = name
    player.append("EFHK")
    
    attempt = 5
    got_caught = False

    airport_coordinates = []

    stamina, budget, rate_up, rate_down, max_flight_distance = mode()

    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            player.append(airport_data[i]["deg"])
            break

    player.append(budget)
    player.append(stamina)

    while player[3] > 0 and player[4] > 0:
        os.system("cls")
        print_player_position(airport_data, player)

        print("Budget   : ", player[3], "€")
        print("Stamina  : ", player[4])

        userSelection = decisions()
        
        if userSelection == "1":
            player, got_caught, attempt = money_heist(player, rate_up, rate_down,attempt)
            if got_caught == True:
                break
        elif userSelection == "2":
            price, stamina, new_icao_code, new_coordinates, attempt = escape(airport_coordinates, max_flight_distance, player, attempt)
            if new_icao_code is not None:
                player = update_player(player, price, stamina, new_icao_code, new_coordinates)

        if player[3] <= 0:
            print("You run out of money")
            print("You lost")
            break
        elif player[4] <= 0:
            print("YOu run out of stamina (too tired to go anywhere)")
            print("You lost")
            break
    input("Press Enter to continue...")

    return


def mode():
    print("Please select the game's mode:")
    print("1- Easy")
    print("2- Hard")
    
    play_mode = input("Your selection: ")
    if play_mode == "1":
        stamina = 1000
        budget = 10000
        rate_up = 1.0
        rate_down = 0
        travel_distance = 1000
    elif play_mode == "2":
        stamina = 700
        budget = 5000
        rate_up = 0.5
        rate_down = 0
        travel_distance = 800
    return stamina, budget, rate_up, rate_down, travel_distance


# MAIN
random.seed()
player = [""]  # player = ['name', 'position_code', coordinates, budget, stamina]

# Fetch all data from database
airport_data = database.get_datalist()

os.system("cls")
name = input("Input name: ")
os.system("cls")

while True:
    userInput = print_mainmenu()  # Print the main menu
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