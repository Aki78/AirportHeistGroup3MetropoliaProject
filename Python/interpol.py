import random
import helper
import database

random.seed()

def interpol_position_and_movement(airport_data, interpol_data):
    airport_coordinates = []
    airport_coordinates.extend(database.get_coordinates())

    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == interpol_data[0]:
            print("The interpol is now at", airport_data[i]["country"])
            print("Watch out for them")

    interpol_position_name_list = helper.get_possible_flights(1000, interpol_data[1], airport_coordinates)
    
    print("Their possible next destination")
    
    for i in range(len(airport_data)):
        for name in interpol_position_name_list:
            if airport_data[i]["name"] == name:
                print(airport_data[i]["country"])
    
    #Random destination
    limit = len(interpol_position_name_list) - 1
    random_move = random.randint(0, limit)
    interpol_next_destination_name = interpol_position_name_list[random_move]

    #Change interpol code and deg
    for i in range(len(airport_data)):
        for name in interpol_position_name_list:
            if airport_data[i]["name"] == interpol_next_destination_name:
                interpol_position_code = airport_data[i]["ident"]
                interpol_position_deg = airport_data[i]["deg"]
    
    return interpol_position_code, interpol_position_deg

def update(interpol_possible_move_code, interpol_possible_move_deg, interpol):
    interpol[0] = interpol_possible_move_code
    interpol[1] = interpol_possible_move_deg
    return interpol
