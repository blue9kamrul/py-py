import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

n = int(input())
t = gi()
mn = t[0]
mx = t[0]
c = 0
for i in range(1, n, 1):
    if t[i] > mx:
        c += 1
        mx = t[i]
    if t[i] < mn:
        c += 1
        mn = t[i]
print(c)