import random
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

def interpol_index():
    pass