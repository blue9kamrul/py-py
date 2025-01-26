import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

s = gs()

res = []
i = 0
ln = len(s)
while i < ln:
    if s[i] == ".":
        res.append(0)
        
    elif i + 1 < ln and s[i] == "-" and s[i+1] == ".":
        res.append(1)
        i += 1
        
    elif i + 1 < ln and s[i] == "-" and s[i + 1] == "-":
        res.append(2)
        i += 1
        
    i += 1
    

print("".join(map(str,res)))
    