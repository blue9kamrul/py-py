import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())

for i in range(n):
    c = 0
    p = gi()
    r = p[2] - p[1]
    if p[0] + p[1] == r:
        c += 1
    if p[1] + r == p[2]:
        c += 1
    if p[2] + r ==  p[3]:  
        c += 1
    print(c)   
