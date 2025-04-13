#accepted

import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())


for i in range(t):
    n, m, l, r = gi()
    target = n - m
    l = abs(l)
    for j in range(target):
        if l <= r:
            r -= 1
        else: 
            l -= 1
    print(-l, r) 