import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    a, b, c = gi()
    if a + b >= 10:
        print("YES")
    elif a + c >= 10:
        print("YES")
    elif b + c >= 10:
        print("YES")
    else: 
        print("NO")