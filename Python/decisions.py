import random
import database
import os
import helper
import gfuncs
import prints

def mode():
    print("Please select the game's mode:")
    print("1- Easy")
    print("2- Hard")
    
    play_mode = input("Your selection: ")

    if play_mode == "1" or play_mode == "Easy":
        return 5000, 10000, 1.0, 0, 1000
    elif play_mode == "2" or play_mode == "Hard":
        return 2500, 5000, 0.75, 0.25, 800
    #return stamina, budget, rate_up, rate_down, travel_distance

    if play_mode == "1" or play_mode == "Easy":
        return 5000, 10000, 1.0, 0, 1000
    elif play_mode == "2" or play_mode == "Hard":
        return 2500, 5000, 0.75, 0.25, 800
    #return stamina, budget, rate_up, rate_down, travel_distance

def heist_decision(): #Input
    print("-> Heist")
    print("-> Escape")
    print("")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "Heist" and str(userInput) != "Escape":
            print("Invalid input")
        else:
            break

    print(userInput)
    return userInput

def money_heist(player, rate_upper, rate_lower, attempt):
    steal_rate = round(gfuncs.theft_success_rate() * 100) / 100
    stolen_money = gfuncs.theft_success_earnings_gauss()
    
    if attempt > 0:
        prints.steal_rate_and_decision(steal_rate, attempt, stolen_money)

        while True:
            userInput = input("Input: ")

            if str(userInput) != "Steal" and str(userInput) != "Wait":
                print("Invalid input")
            else:
                break

        if userInput == "Steal":
            #stolen_money = gfuncs.theft_success_earnings_gauss()
            #print("You will get", stolen_money, "€")

            true_rate = random.uniform(rate_lower, rate_upper)
            # print("true rate", true_rate)
            if true_rate <= steal_rate:
                print("Steal successful")
                player[3] += stolen_money
                attempt -= 1
                input("Press Enter to continue")
            else:
                print("You got caught by local police")
                print("You lost")
                input("Press Enter to continue")
                
                return player, True, attempt
        elif userInput == "Wait":
            attempt -= 1
    
    elif attempt == 0:
        print("You got caught by the local police")
        got_caught = True
        return player, got_caught, attempt
    
    return player, False, attempt


def escape(airport_data, airport_coordinates, max_flight_distance, player, attempt):

    airport_coordinates = []
    possible_flights_name = []
    amount_of_possible_flights = 0

    print("Possible airports:")

    airport_coordinates.extend(database.get_coordinates())

    # Return name list of possible airports
    possible_flights_name = helper.get_possible_flights(max_flight_distance, player[2], airport_coordinates)

    # Check amount of possible airports (for later use)
    amount_of_possible_flights = helper.print_possible_flights(airport_data, possible_flights_name, airport_coordinates)

    # Player choose the airport and return the icao code of destination
    price, stamina, new_icao_code, new_coordinates = player_airport_selection(possible_flights_name,
                                                                                airport_coordinates, player[2],
                                                                                amount_of_possible_flights)

    if new_icao_code is not None:
        #print("Waiting for new code 1", new_icao_code)
        return price, stamina, new_icao_code, new_coordinates, 5
    else:
        return 0, 0, None, (0, 0), attempt


def player_airport_selection(name_list, coordinates, player_coordinates, amount_of_possible_flights):
    userInput = "0"

    # Input airport decision (fix later)
    while True:
        userInput = input("Input: ").strip()

        if userInput == "" or type(int(userInput)) is not int:
            print("Invalid input")
        else:
            selection = int(userInput) - 1
            break

    price, stamina, icao_code, new_coordinates = helper.print_flight_details(name_list, selection, player_coordinates)

    print("Do you want to travel?")
    print("-> Travel")
    print("-> Stay")
    print("")

    # Input decision (also fix later)
    while True:
        userInput = input("Input: ")

        if str(userInput) != "Travel" and str(userInput) != "Stay":
            print("Invalid input")
        else:
            break

    if userInput == "Travel":
        #print("Waiting for new code 2", icao_code)
        return price, stamina, icao_code, new_coordinates
    elif userInput == "Stay":
        return 0, 0, None, (0, 0)
