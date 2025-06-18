n = int(input())

def counter(number:int):
    numbers = list(range(1, number + 1))
    total = sum(numbers)
    if number == 1:
        return f"{number} = {number}"
    else:
        if number >= 1 and number <= 1000:
            return " + ".join(map(str, numbers)) + " = " + str(total)

print(counter(n))