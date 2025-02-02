import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    g = 0
    a, b, c, d = gi()
    if a < b:
        g += 1
    if a < c:
        g += 1
    if a < d:
        g += 1
    print(g)