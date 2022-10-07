import os
import settings
import database
import random
import prints
import decisions
import interpol

def update_player(player, price, stamina, new_icao_code, new_coordinates):
    player[1] = new_icao_code
    player[2] = new_coordinates
    player[3] -= price
    player[4] -= stamina
    return player

def run_game(airport_data):
    os.system("cls")

    player = [""]   # player = ['name', 'icao_code', coordinates, budget, stamina]
    player[0] = name
    player.append("EFHK")

    

    interpol_info = [""] #interpol = ['icao_code', coordinates]
    interpol_info[0] = "LFBD"
    interpol_info.append((44.8283, -0.715556))
    
    attempt = 5
    got_caught = False

    airport_coordinates = []

    stamina, budget, rate_up, rate_down, max_flight_distance = settings.mode()

    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == player[1]:
            player.append(airport_data[i]["deg"])
            break

    player.append(budget)
    player.append(stamina)

    while player[3] > 0 and player[4] > 0 and got_caught is False:
        os.system("cls")
        
        interpol.print_interpol_position(airport_data, interpol_info)
        print("")
        prints.print_player_position(airport_data, player)

        userSelection = decisions.heist_decision()
        
        if userSelection == "1":
            player, got_caught, attempt = decisions.money_heist(player, rate_up, rate_down,attempt)
            if got_caught == True:
                break
        elif userSelection == "2":
            price, stamina, new_icao_code, new_coordinates, attempt = decisions.escape(airport_coordinates, max_flight_distance, player, attempt)
            if new_icao_code is not None:
                player = update_player(player, price, stamina, new_icao_code, new_coordinates)

        if player[3] <= 0:
            print("You run out of money")
            print("You lost")
            break
        elif player[4] <= 0:
            print("You run out of stamina (too tired to go anywhere)")
            print("You lost")
            break
        
        interpol_position = interpol.movement()    


    input("Press Enter to continue...")

    return

# MAIN
random.seed() 

# Fetch all data from database
airport_data = database.get_datalist()

os.system("cls")
name = input("Input name: ")
os.system("cls")

while True:
    userInput = prints.print_mainmenu(name)  # Print the main menu
    print(userInput)

    if userInput == "1":
        run_game(airport_data)
    elif userInput == "2":
        prints.print_settings()
    elif userInput == "3":
        prints.print_instructions()
    elif userInput == "4":
        prints.print_credits()
    elif userInput == "5":
        os.system("cls")
        input("Press Enter to exit...")
        break