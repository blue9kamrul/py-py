import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
t = gi()

sum = 0
for i in range(n):
    sum = sum + t[i]

sum = sum / (n*100)
print(round(sum*100,12))
