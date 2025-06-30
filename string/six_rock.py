
def six_rock(rock_name:str):
    items = {
        'space':'blue',
        'mind':'yellow',
        'reality':'red',
        'power':'purple',
        'time':'green',
        'soul':'orange'
    }
    if rock_name not in items.keys():
        return -1
    for rock , color in items.items():
        if rock_name == rock:
            return color
    

print(six_rock(rock_name=input()))