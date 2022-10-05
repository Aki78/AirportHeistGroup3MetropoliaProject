import os
import time
def main_screen():
    os.system('cls')
    while True:
        print("Welcome to airport heist!")
        print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")
        print()
        user_input = str(input("What do you want to do: "))

        if user_input == "" or int(user_input) > 5 or int(user_input) < 1:
            print("unknown input")
            main_screen()
        if user_input == "2":
            setting_screen()
        if user_input == "3":
            instructions()
        if user_input == "4":
            credits()
        if user_input == "5":
            break

def setting_screen():
    os.system('cls')
    while True:
        print("Settings")
        print("Choose the game level\n1. Easy \n2. Hard")
        settings_input = str(input("What do you want to do: "))

        if settings_input == "" or int(settings_input) > 3 or int(settings_input) < 1:
            print("unknown input")
            setting_screen()
        if settings_input == "1":
            print("Good choice!")
            time.sleep(1.5)
            main_screen()
        if settings_input == "2":
            print("Good luck!")
            time.sleep(1.5)
            main_screen()

def instructions():
    os.system('cls')
    while True:
        print("Instructions")
        print("Text")
        instructions_input = str(input("Press 'enter' to return to the main menu:"))

        if instructions_input == None:
            print("unknown input")
        else:
            main_screen()

def credits():
    os.system('cls')
    while True:
        print("Credits")
        print("Airport Heist was created by the most awesome of foursomes!\nAki Morooka \nKhai cao \nKiana Aghajani \nFrancesco Natanni\nAll work is our own, so all credit goes to us.")
        credits_input = str(input("Press 'enter' to return to the main menu:"))

        if credits_input == None:
            print("unknown input")
        else:
            main_screen()

main_screen()




