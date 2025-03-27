s = input()

def bime_checker(name:str):
    list_of_char = []
    if len(name) <= 20:
            
            if all(j.islower() for j in name):
                for i in name:
                    list_of_char.append(i)
                if 'm' in list_of_char:
                    return 'No'
                else:
                    return 'Yes'

print(bime_checker(s))