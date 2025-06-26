
# Solution 1
def football_fans(n:str) -> int:
    return len(max(n.split('1')))

# Solution 2
def football_fans(n:str) -> int:
    allowed = ['0', '1']
    for i in n:
        if i not in allowed:
            return -1
    s = n.split('1')
    return len((max(s)))