
def palindrome_number(num:int) -> bool:
    n = ""
    s = list(str(num))
    s.reverse()

    for i in range(len(s)):
        n += s[i]

    if n == str(num):
        return True
    else:
        return False