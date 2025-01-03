import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

s1 = input().strip().lower()
s2 = input().strip().lower()

if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)

