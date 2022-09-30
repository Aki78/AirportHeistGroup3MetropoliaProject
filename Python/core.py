import os

def mainMenu():
    userInput = "0"
    
    while True:
        os.system("cls")

        print("1. Start")
        print("2. Settings")
        print("3. Instructions")
        print("4. Credits")
        print("5. Exit")

        userInput = input("Input: ")

        if userInput == "" or int(userInput) < 0 or int(userInput) > 5:
            print("Invalid input")
        else:
            return int(userInput)






budget = 1000000
co2 = 100000
player = [""]

os.system("cls")
name = input("Input name: ")
os.system("cls")

print("Welcome to flight game")
print("")
print("Hello, "+ str(name) + "!")

while True:
    userInput = mainMenu() #Print the main menu

    if userInput == 1:
        print(userInput)
    elif userInput == 2:
        print(userInput)
    elif userInput == 3:
        print(userInput)
    elif userInput == 4:
        print(userInput)
    elif userInput == 5:
        break
        