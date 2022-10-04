import random
import helper
import numpy as np

def theft_success_earnings_gauss():
    s = np.random.normal(3000, 500, 1)
    return s[0]

def theft_success_rate():
    probability = random.random()
    return 0.5 > probability


def get_ticket_price(distance):
    ticket_price = round(distance * 1.5)
    return ticket_price
