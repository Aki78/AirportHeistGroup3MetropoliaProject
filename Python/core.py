import os
import settings
import database
import random
import prints
import decisions
import interpol
import gfuncs


def init_state():
    os.system("clear")

    player = [""]   # player = ['name', 'icao_code', coordinates, budget, stamina]
    player[0] = name
    player.append("EFHK")

    interpol_info = [""] #interpol = ['icao_code', coordinates]
    interpol_info[0] = "LFBD"
    interpol_info.append((44.8283, -0.715556))
    
    attempt_left = 5
    got_caught = False

    airport_coordinates = []

    stamina, budget, rate_upper, rate_lower, max_flight_distance = settings.mode()

    game_state = {
                    "player":player,
                    "interpol":interpol_info,
                    "got_caught":got_caught,
                    "attempt_left": attempt_left,
                    "airport_coordinates" : airport_coordinates,
                    "stamina" : stamina,
                    "budget" : budget,
                    "rate_upper" : rate_upper,
                    "rate_lower" : rate_lower,
                    "max_flight_distance" : max_flight_distance
                  }

    return game_state


def run_game(airport_data):
    game_state = init_state()

    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == game_state["player"][1]:
            game_state["player"].append(airport_data[i]["deg"])
            break

    game_state["player"].append(game_state["budget"])
    game_state["player"].append(game_state["stamina"])

    while game_state["player"][3] > 0 and game_state["player"][4] > 0 and game_state["got_caught "]is False:
        os.system("clear")
        
        interpol.print_interpol_position(airport_data, game_state["interpol_info"])
        print("")
        prints.print_player_position(airport_data, game_state["player"])

        userSelection = decisions.heist_decision()
        
        if userSelection == "1":
            game_state["player"], got_caught, game_state["attempt_left "]= decisions.money_heist(game_state["player"], game_state["rate_upper"], game_state["rate_lower"],game_state["attempt_left"])
            if got_caught == True:
                break
        elif userSelection == "2":
            price, stamina, new_icao_code, new_coordinates, game_state["attempt_left "]= decisions.escape(game_state["airport_coordinates"], game_state["max_flight_distance"], game_state["player"], game_state["attempt_left"])
            if new_icao_code is not None:
                game_state["player "]= gfuncs.update_player(game_state["player"], price, stamina, new_icao_code, new_coordinates)

        if game_state["player"][3] <= 0:
            print("You run out of money")
            print("You lost")
            break
        elif game_state["player"][4] <= 0:
            print("You run out of stamina (too tired to go anywhere)")
            print("You lost")
            break
        
        game_state["interpol_position "]= interpol.movement()    

    input("Press Enter to continue...")

    return

if __name__ == "__main__":
# MAIN
    random.seed() 
# Fetch all data from database
    airport_data = database.get_datalist()

    os.system("clear")
    name = input("Input name: ")
    os.system("clear")

    while True:
        userInput = prints.print_mainmenu(name)  # Print the main menu
        print(userInput)

        if userInput == "Start":
            run_game(airport_data)
        elif userInput == "Settings":
            prints.print_settings()
        elif userInput == "Instructions":
            prints.print_instructions()
        elif userInput == "Credits":
            prints.print_credits()
        elif userInput == "Exit":
            os.system("clear")
            input("Press Enter to exit...")
            break
