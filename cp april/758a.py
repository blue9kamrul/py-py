import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
a = gi()
mx = max(a)
c = 0

for i in range(n):
    if a[i] < mx:
        c += mx - a[i]

print(c)




