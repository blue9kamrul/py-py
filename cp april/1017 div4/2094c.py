#acccepted

import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a = gi()
        
        for k in a:
            if k not in s:
                s.append(k)
    full = list(range(min(s), max(s) + 1))
    missing = list(set(full) - set(s))
    
    if missing == [] and 1 not in s:
        s.insert(0,1)
    elif missing == []:
        s.insert(0,2*n)
    else:
        s.insert(0,*missing)            
    print(*s)