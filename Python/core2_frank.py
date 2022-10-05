import os
def main_screen():
    while True:
        print("Welcome to airport heist!")
        print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")
        print()
        user_input = str(input("What do you want to do: "))

        if user_input == "" or int(user_input) > 5 or int(user_input) < 1:
            print("unknown input")
            main_screen()
        elif user_input == "2":
            setting_screen()

        else:
            return user_input

def setting_screen():
    while True:
        print("Settings")
        print("1. Easy \n2. Hard \n3. Return to main menu")
        settings_input = str(input("What do you want to do: "))

        if settings_input == "" or int(settings_input) > 3 or int(settings_input) < 1:
            print("unknown input")
        elif settings_input == "3":
            main_screen()
        else:
            return settings_input


main_screen()




