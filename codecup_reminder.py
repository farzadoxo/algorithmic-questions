user_input = int(input("Enter round of codecup bootcamp :"))

def codecup_reminder(round:int):
    return "Hello CodeCup {}!".format(round)

print(codecup_reminder(user_input))