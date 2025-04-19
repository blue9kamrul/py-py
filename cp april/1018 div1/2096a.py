import sys

# sys.stdout = open('cp april/output.txt', 'w')
# # sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    small = big = 0
    target = 1
    res = []
    for j in range(len(s)):
        if s[j] == "<":
            small += 1
        else: 
            big += 1
    
    target += small
    
    res.append(target)
    st = bt = target
    #ok
    for j in range(len(s)-1):
        if s[j] == "<":
            st -=  1
            res.append(st)
            # print(st,bt)
        else: 
            bt +=  1  
            res.append(bt)
            # print(st,bt)
    print(*res)