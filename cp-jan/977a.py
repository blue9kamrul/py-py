import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n, k = gi()

for i in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n /= 10

print(int(n))