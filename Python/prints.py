import os
from colorama import Fore , Back , Style 

def print_start(name):
    print("Hello, " + str(name) + "!")
    print("Welcome to flight game!")
    print("")
    print(Fore.MAGENTA + "->" + Style.RESET_ALL+ " Start")
    print(Fore.MAGENTA +"->" + Style.RESET_ALL+ " Settings")
    print(Fore.MAGENTA +"->" + Style.RESET_ALL+ " Instructions")
    print(Fore.MAGENTA +"->" + Style.RESET_ALL+ " Credits")
    print(Fore.MAGENTA +"->" + Style.RESET_ALL+  " Exit")

def print_instructions():
    print("This is the instructions:")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You will be assigned a random destination.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You are limited by budget and stamina.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You have to buy tickets to travel.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " In order to acquire money, you have to steal.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " you can get caught by the interpol and lose the game.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You will be informed of the interpol's possible destination")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You are restricted to airports with-in a certain distance.")
    print(Fore.LIGHTBLUE_EX + "--" + Style.RESET_ALL+ " You will lose if you go under stamina or budget.")

    input("Press Enter to go back...")
    return

def print_settings():
    print("Under developments. Please come back later.")
    input("Press Enter to go back...")
    return

def print_credits():
    print("The master mindes behind this game are:")
    print("-> Aki")
    print("-> Frank")
    print("-> Khai")
    print("-> Kiana")
    print("These people all had to escape from prison at some point in their lives,")
    print("So they have gathered around and made their experinces into a game.")
    print("You can use this game to prepare for in real life situations.")
    input("Press Enter to go back...")
    return

def print_player_position(airport_data, player):
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            print("You are in", airport_data[i]["country"])
            print("Airport  : ", airport_data[i]["name"])
            print("Budget   : ", player[3], "€")
            print("Stamina  : ", player[4])
            print("")
            break
    return

def print_mainmenu(name):
    userInput = 0

    while True:

        print_start(name)

        userInput = input("Input: ")

        if userInput not in  ["Start", "Settings", "Instructions", "Credits", "Exit"] :
            print("Invalid input")
            input("Press Enter to continue...")
        else:
            return str(userInput)

def steal_rate_and_decision(steal_rate, attempt, stolen_money):
    if attempt > 1:
            print("Attempts remaining:", attempt - 1)
            print("Your are about to steal more money")
    elif attempt == 1:
        print("Last attempt")
        print("You have to steal or you will get caught the next time")

    print("You will get", stolen_money, "€")        
    print("Successful stealing rate: " + str(round(steal_rate * 100)) + "%")
    print("-> Steal")
    print("-> Wait")
    print("")
    return