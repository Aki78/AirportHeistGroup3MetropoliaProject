import os


def print_start(name):
    print("Welcome to flight game")
    print("")
    print("Hello, " + str(name) + "!")

    print("1. Start")
    print("2. Settings")
    print("3. Instructions")
    print("4. Credits")
    print("5. Exit")

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

def print_settings():
    os.system("cls")
    print("Under developments. Please come back later.")
    input("Press Enter to continue...")
    return

def print_credits():
    os.system("cls")
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
        os.system("cls")

        print_start(name)

        userInput = input("Input: ")

        if userInput == "" or int(userInput) < 1 or int(userInput) > 5:
            print("Invalid input")
            input("Press Enter to continue...")
        else:
            return str(userInput)

def steal_rate_and_decision(steal_rate):
    print("Your are about to steal more money")
    print("Successful stealing rate: ", steal_rate * 100, "%")
    print("1. Steal")
    print("2. Later")
    print("")
    