c = int(input())

def sheep_counter(c:int):
    if c > 4:
        if c % 4 == 0:
            return int(c/4)
    
print(sheep_counter(c))