import os
import time
import numpy as np

setting_input = None
def theft_success_earnings_gauss():
    if "1" == setting_input:
        s = np.random.normal(3000, 500, 1)
    if "2" == setting_input:
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
            print("Invalid input, please select one of the following options.")
            main_screen()
        if user_input == "1":
            print("game not created yet")
        if user_input == "2" or user_input == "Settings":
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
        time.sleep(1)
        input("1 - You are limited by budget and stamina.Press Enter to continue...")
        input("2 - You have to buy tickets to travel. Press Enter to continue...")
        input("3 - In order to acquire money, you have to steal. Press Enter to continue...")
        input("4 - You can get caught by the interpol, but you are informed about the odds. Press Enter to continue...")
        input("5 - You can see in which possible cities the interpol will be, but not where they will go next. Press Enter to continue...")
        input("6 - You are restricted to airports with-in a certain distance. Press Enter to continue...")
        input("7 - You will lose if you go under stamina or budget. Press Enter to continue...")
        input("Press Enter to continue...")

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




