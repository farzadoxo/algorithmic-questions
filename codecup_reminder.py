r = int(input())

def codecup_reminder(round:int):
    if round >= 1 and round <= 100 :
        return f"Hello CodeCup {round}!"

print(codecup_reminder(r))