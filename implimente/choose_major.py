
def choose_major(location:str) -> str:
    allowed = {
        'EAST':'YES',
        'NOT EAST':'NO'
    }

    if location.upper() not in allowed:
        return -1
    for loc , ans in allowed.items():
        if location.upper() == loc:
            return ans