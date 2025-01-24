import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

x = gi()
x.sort()

c = x[1] - x[0] + x[2] - x[1]
print(c)
