def print_interpol_position(airport_data, interpol):
    for i in range(len(airport_data)):
        if airport_data[i]["ident"] == interpol[0]:
            print("The interpol is now at", airport_data[i]["country"])
            print("Watch out for them")
    return

def movement():
    return "EFHK"

