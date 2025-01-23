import sys
import math

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())

    n = math.ceil(n / 2) - 1
    print(n)