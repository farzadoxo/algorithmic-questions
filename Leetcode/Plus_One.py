def plus_one(digits:list[int]) -> list[int]:
        res = ""
        res2 = 0
        lst = []
        for i in digits:
            res += str(i)
        res2 = int(res)
        res2 += 1
        for j in str(res2):
            lst.append(int(j))
        return lst

