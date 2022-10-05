
def main_screen():
    print("Welcome to airport heist!")
    print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")

main_screen()
user_input = input("What do you want to do: ")

if user_input == "" or user_input > 5 or user_input < 1:
    print("unknown input")
    main_screen()

#if user_input == "1":

if user_input == "2":
    print("Settings")
    print("1. Easy \n2. Hard \n3. Return to main menu")
    settings_input = input("What do you want to do: ")
    if user_input == "" or user_input > 3 or user_input < 1:
        print("unknown input")
        main_screen()

