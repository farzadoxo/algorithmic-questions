
def addDigits(num:int) -> bool:
    
    if num == 0 or len(list(str(num))) <= 1:
        return num
    sum_num = 0
    for j in list(str(num)):
        sum_num += int(j)
    
    return addDigits(sum_num)