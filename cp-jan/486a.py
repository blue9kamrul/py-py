import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())

if n % 2 == 0:
    print(int(n/2))
else:
    print(int(-((n//2)+1)))