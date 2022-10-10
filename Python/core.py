import os
import settings
import database
import random
import prints
import decisions
import interpol
import gfuncs
import interpol


def init_state():

    player = [""]   # player = ['name', 'icao_code', coordinates, budget, stamina]
    player[0] = "Aki" # Change to name input later
    player.append("EFHK")

    interpol = [""] #interpol = ['icao_code', coordinates]
    interpol[0] = "LFBD"
    interpol.append((44.8283, -0.715556))
    
    attempt_left = 5
    got_caught = False

    airport_coordinates = []

    stamina, budget, rate_upper, rate_lower, max_flight_distance = settings.mode()
    airport_data = database.get_datalist()
    lost = False


    game_state = {
                    "airport_data": airport_data,
                    "player": player,
                    "interpol": interpol,
                    "got_caught": got_caught,
                    "attempt_left": attempt_left,
                    "airport_coordinates": airport_coordinates,
                    "stamina": stamina,
                    "budget": budget,
                    "rate_upper": rate_upper,
                    "rate_lower": rate_lower,
                    "max_flight_distance": max_flight_distance,
                    "lost": lost
                  }
                  
    
    for i in range(len(game_state["airport_data"])):
        if game_state["airport_data"][i]["ident"] == game_state["player"][1]:
            game_state["player"].append(game_state["airport_data"][i]["deg"])
            break

    game_state["player"].append(game_state["budget"])
    game_state["player"].append(game_state["stamina"])
    print("Returning game state:", game_state)

    return game_state


def run_game():
    #init state
    game_state = init_state()

    while game_state["player"][3] > 0 and game_state["player"][4] > 0 and game_state["got_caught"] is False:
        
        interpol.print_interpol_position(game_state["airport_data"], game_state["interpol"])
        print("")
        prints.print_player_position(game_state["airport_data"], game_state["player"])

        userSelection = decisions.heist_decision()
        
        if userSelection == "Heist":
            game_state["player"], got_caught, game_state["attempt_left "] = decisions.money_heist(game_state["player"], game_state["rate_upper"], game_state["rate_lower"],game_state["attempt_left"])
            if got_caught == True:
                break
        elif userSelection == "Escape":
            price, stamina, new_icao_code, new_coordinates, game_state["attempt_left "]= decisions.escape(game_state["airport_coordinates"], game_state["max_flight_distance"], game_state["player"], game_state["attempt_left"])
            if new_icao_code is not None:
                game_state["player "]= gfuncs.update_player(game_state["player"], price, stamina, new_icao_code, new_coordinates)

        if game_state["player"][3] <= 0:
            #send lost signal
            game_state["lost"] = True
            print("You run out of money")
            print("You lost")
            break
        elif game_state["player"][4] <= 0:
            #send lost signal
            game_state["lost"] = True
            print("You run out of stamina (too tired to go anywhere)")
            print("You lost")
            break
        
        game_state["interpol_position "] = interpol.movement()

    input("Press Enter to continue...")

    return

if __name__ == "__main__":
    random.seed() 

    name = input("Input name: ")

    while True:
        userInput = prints.print_mainmenu(name)  # Print the main menu
        print(userInput)

        if userInput == "Start":
            run_game()
        elif userInput == "Settings":
            prints.print_settings()
        elif userInput == "Instructions":
            prints.print_instructions()
        elif userInput == "Credits":
            prints.print_credits()
        elif userInput == "Exit":
            input("Press Enter to exit...")
            break
