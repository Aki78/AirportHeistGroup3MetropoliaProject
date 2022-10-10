import random
import helper
import numpy as np

def theft_success_earnings_gauss():
    s = np.random.normal(3000, 500, 1)
    return round(s[0])

def theft_success_rate():
    return random.random()

def get_ticket_price(distance): 
    return round(distance * 1.5)

def get_stamina_consumptions(distance):
    return round(distance / 2)

def interpol_index(deg_list, coordinates):
    new_list =  helper.get_possible_flights(300, coordinates, deg_list)
    return random.choice(new_list)

def update_player(player, price, stamina, new_icao_code, new_coordinates):
    player[1] = new_icao_code
    player[2] = new_coordinates
    player[3] -= price
    player[4] -= stamina
    return player
