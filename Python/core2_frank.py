import os
def main_screen():
    print("Welcome to airport heist!")
    print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")
    user_input = str(input("What do you want to do: "))

    if user_input == "" or int(user_input) > 5 or int(user_input) < 1:
        print("unknown input")
    return user_input

def setting_screen():
    print("Settings")
    print("1. Easy \n2. Hard \n3. Return to main menu")
    settings_input = str(input("What do you want to do: "))
    return settings_input

while True:
    main_screen()

    #if main_screen() == "1":

    if main_screen() == 2:
        setting_screen()
        if setting_screen() == "" or int(setting_screen()) > 3 or int(setting_screen() < 1):
            print("unknown input")
            setting_screen()

