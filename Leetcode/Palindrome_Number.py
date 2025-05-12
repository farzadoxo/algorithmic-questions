num_list = [121,-121,10]


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



if __name__ == "__main__":
    for i in num_list:
        print(palindrome_number(num=i))
