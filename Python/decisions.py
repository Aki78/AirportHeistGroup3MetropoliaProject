import random
import database
import os
import helper
import gfuncs


def heist_decision(): #Input
    print("Choice> Heist")
    print("Choice> Escape")
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
    os.system("clear")
    steal_rate = round(gfuncs.theft_success_rate() * 100) / 100
    if attempt > 0:
        print("Attemps remaining:", attempt - 1)
        print("Your are about to steal more money")
        print("Successful stealing rate: ", steal_rate * 100, "%")
        print("Choice> Steal")
        print("Choice> Wait")
        print("")

    while True:
        userInput = input("Input: ")

        if str(userInput) != "Steal" and str(userInput) != "Wait":
            print("Invalid input")
        else:
            break

    if userInput == "Steal":
        os.system("clear")
        stolen_money = gfuncs.theft_success_earnings_gauss()
        print("Got", stolen_money, "€")

        true_rate = random.uniform(rate_lower, rate_upper)
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

        if userInput == "Steal":
            os.system("clear")
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
    elif userInput == "Wait":
        attempt -= 1
    if attempt == 0:
        print("You got caught!")
        got_caught = True
        return player, got_caught, attempt
    return player, False, attempt


def escape(airport_coordinates, max_flight_distance, player,attempt):
    attempt = 5
    os.system("clear")

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
        else:
            selection = int(userInput) - 1
            break

    os.system("clear")
    price, stamina, icao_code, new_coordinates = helper.print_flight_details(name_list, selection, player_coordinates)

    print("Travel")
    print("Stay")
    print("")

    # Input decision (also fix later)
    while True:
        userInput = input("Input: ")

        if str(userInput) != "Stravel" and str(userInput) != "Stay":
            print("Invalid input")
        else:
            break

    if int(userInput) == "Travel":
        #print("Waiting for new code 2", icao_code)
        return price, stamina, icao_code, new_coordinates
    elif int(userInput) == "Stay":
        return 0, 0, None, (0, 0)
