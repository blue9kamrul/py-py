#accepted

import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
c = ''

for i in range(n):
    s = input()
    c += s[0]
    for j in range(len(s)):    
        if s[j] == ' ':
            c += s[j+1]
    print(c)
    c = ''

        

