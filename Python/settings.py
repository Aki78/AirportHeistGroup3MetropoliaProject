def mode():
    print("Please select the game's mode:")
    print("1- Easy")
    print("2- Hard")
    
    play_mode = input("Your selection: ")

    if play_mode == "1" or play_mode == 'Easy':
        stamina = 1000
        budget = 10000
        rate_up = 1.0
        rate_down = 0
        travel_distance = 1000
    elif play_mode == "2" or play_mode == 'Hard':
        stamina = 700
        budget = 5000
        rate_up = 0.5
        rate_down = 0
        travel_distance = 800
    return stamina, budget, rate_up, rate_down, travel_distance