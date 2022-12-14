import os
import helper
import database
import random
import prints
import decisions
import interpol
import gfuncs
import time


def init_state():

    player = ["steve", "jenni", "john", "emma"]   # player = ['name', 'icao_code', coordinates, budget, stamina]
    player[0] = "Aki" # Change to name input later
    player.append("EFHK")

    interpol_data = [""] #interpol_data = ['icao_code', coordinates]
    interpol_data[0] = "LFBD"
    interpol_data.append((44.8283, -0.715556))

    airport_data = database.get_datalist()
    
    airport_coordinates = []
    attempt_left = 5
    got_caught = False
    lost = False

    destination_code, destination_country = helper.chooose_destination(airport_data) 
    destination_reached = False

    stamina, budget, rate_upper, rate_lower, max_flight_distance = decisions.mode()
    print(budget)
    print(stamina)

    game_state = {
                    "airport_data" : airport_data,
                    "player" : player,
                    "interpol_data" : interpol_data,
                    "got_caught" : got_caught,
                    "attempt_left" : attempt_left,
                    "airport_coordinates" : airport_coordinates,
                    "stamina" : stamina,
                    "budget" : budget,
                    "rate_upper" : rate_upper,
                    "rate_lower" : rate_lower,
                    "max_flight_distance" : max_flight_distance,
                    "lost" : lost,
                    "destination_code" : destination_code,
                    "destination_country" : destination_country,
                    "destination_reached" : destination_reached
                  }
    
    for i in range(len(game_state["airport_data"])):
        if game_state["airport_data"][i]["ident"] == game_state["player"][1]:
            game_state["player"].append(game_state["airport_data"][i]["deg"])
            break

    game_state["player"].append(game_state["budget"])
    game_state["player"].append(game_state["stamina"])
    
    print("Returning game state from init():", game_state)

    return game_state


def run_game():
    #init state
    game_state = init_state()

    while game_state["lost"] is False and game_state["got_caught"] is False and game_state["destination_reached"] is False:
        #Print interpol position
        interpol_possible_move_code, interpol_possible_move_deg = interpol.interpol_position_and_movement(  game_state["airport_data"], 
                                                                                                            game_state["interpol_data"])
        print("")
        
        #Print destination country
        print("Your destination is", game_state["destination_country"])

        prints.print_player_position(game_state["airport_data"], game_state["player"])

        userSelection = decisions.heist_decision()
        
        if userSelection == "Heist":
            game_state["player"], got_caught, game_state["attempt_left"] = decisions.money_heist(   game_state["player"], 
                                                                                                    game_state["rate_upper"], 
                                                                                                    game_state["rate_lower"],
                                                                                                    game_state["attempt_left"])
            if got_caught == True:
                break
        elif userSelection == "Escape":
            price, stamina, new_icao_code, new_coordinates, game_state["attempt_left"] = decisions.escape(  game_state["airport_data"], 
                                                                                                            game_state["airport_coordinates"], 
                                                                                                            game_state["max_flight_distance"], 
                                                                                                            game_state["player"], 
                                                                                                            game_state["attempt_left"])
            if new_icao_code is not None:
                game_state["player"] = gfuncs.update_player(game_state["player"], price, stamina, new_icao_code, new_coordinates)

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
        
        if game_state["destination_code"] == game_state["player"][1]:
            #send won signal
            game_state["destination_reached"] = True 
            print("You reached the destination without getting captured")
            print("You won")
            break
            
        game_state["interpol_data"] = interpol.update(interpol_possible_move_code, interpol_possible_move_deg, game_state["interpol_data"])   
        
        if game_state["player"][1] == game_state["interpol_data"][0]:
            #send lost signal
            game_state["lost"] = True
            print("Interpol caught you")
            print("You lost")

    return

if __name__ == "__main__":
    random.seed() 

    # name = input("Input name: ")
    name = "something"
            
    while True:
        userInput = prints.print_mainmenu(name)  # Print the main menu
        if userInput == "Start":
            run_game()
