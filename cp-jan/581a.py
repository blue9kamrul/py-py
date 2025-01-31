import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

a, b = gi()

d =(max(a,b) - min(a,b) ) // 2
c = min(a,b)

print(c, d)
