import os
import time
import numpy as np

def theft_success_earnings_gauss():
    if setting_screen() = "1":
        s = np.random.normal(3000, 500, 1)
    if setting_screen() = "2":
        s = np.random.normal(2000, 500, 1)
    return round(s[0])
def main_screen():
    os.system('clear')
    while True:
        print("Welcome to airport heist!")
        print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")
        print()
        user_input = str(input("What do you want to do: "))

        if user_input == "" or int(user_input) > 5 or int(user_input) < 1:
            print("Unknown input, please try again.")
            main_screen()
        if user_input == "2":
            setting_screen()
        if user_input == "3":
            instructions()
        if user_input == "4":
            credits()
        if user_input == "5":
            break
        return

def setting_screen():
    os.system('clear')
    while True:
        print("Settings")
        print("Choose the game level\n1. Easy \n2. Hard")
        settings_input = str(input("What do you want to do: "))

        if settings_input == "" or int(settings_input) > 3 or int(settings_input) < 1:
            print("Unknown input, please try again.")
            setting_screen()
        if settings_input == "1":
            print("Good choice!")
            time.sleep(1.5)
            main_screen()
        if settings_input == "2":
            print("Good luck!")
            time.sleep(1.5)
            main_screen()
        return settings_input

def instructions():
    os.system('clear')
    while True:
        print("Instructions")
        print("The first step is to decide if you will STEAL or ESCAPE."
              "\nYou can choose to STEAL money to increase your wealth."
              "\nYou will be shown the odds of your success."
              "\nIf you like dont like your odds, you can try to escape or try to steal again with different odds."
              "\nYou can decide to ESCAPE instead."
              "\nYou will be taken to a map showing all airports with-in your reach and budget."
              "\nKeep an eye on where interpol is searching for you and avoid getting too close to them!"
              "\nChoose the airport you wish to travel to, but be aware of your stamina level, as the more you travel, the more you tire."
              "\nIf you are caught, run out of stamina or run our of money, its game-over, as interpol will take you back to jail!")

        instructions_input = str(input("Press 'Enter' to return to the main menu:"))

        if instructions_input == None:
            print("Unknown input, please try again.")
        else:
            main_screen()
        return

def credits():
    os.system('clear')
    while True:
        print("Credits")
        print("Airport Heist was created by the most awesome of foursomes!\nAki Morooka \nKhai cao \nKiana Aghajani \nFrancesco Natanni\nAll work is our own, so all credit goes to us.")
        credits_input = str(input("Press 'Enter' to return to the main menu:"))

        if credits_input == None:
            print("Unknown input, please try again.")
        else:
            main_screen()
        return
main_screen()




