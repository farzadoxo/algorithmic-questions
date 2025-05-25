
def decimal_to_binary(n:int):
    if n == 0:
        return
    else:
        for i in str(n):
            print(n % 2)


print(decimal_to_binary(n=23))