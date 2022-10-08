import os


def print_start(name):
    print("Welcome to flight game")
    print("Hello, " + str(name) + "!")

    print("Choice> Start")
    print("Choice> Settings")
    print("Choice> Instructions")
    print("Choice> Credits")
    print("Choice> Exit")

def print_instructions():
    os.system("clear")
    print("This is the instructions")
    print("-- You are limited by budget and stamina.")
    print("-- You have to by tickets to travel.")
    print("-- In order to acquire money, you have to steal.")
    print("-- You can get caught by the interpol, but you are informed about the odds.")
    print("-- You can see in which possible cities the interpol will be, but not where they will go next.")
    print("-- You are restricted to airports with-in a certain distance.")
    print("-- You will lose if you go under stamina or budget.")

    input("Press Enter to continue...")
    return

def print_settings():
    os.system("clear")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
    return

def print_credits():
    os.system("clear")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
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
        os.system("clear")

        print_start(name)

        userInput = input("Input: ")

        if userInput not in  ["Start", "Settings", "Instructions", "Credits", "Exist"] :
            print("Invalid input")
            input("Press Enter to continue...")
        else:
            return str(userInput)

def steal_rate_and_decision(steal_rate):
    print("Your are about to steal more money")
    print("Successful stealing rate: ", steal_rate * 100, "%")
    print("Choice> Steal")
    print("Choice> Later")
    print("")
    
