print("Welcome to airport heist!")
print("1. Play \n2. Settings \n3. Instructions \n4. Credits \n5. Exit")
user_input = input("What do you want to do: ")

if user_input == "" or user_input > 5 or user_input < 1:
    print("unknown input")