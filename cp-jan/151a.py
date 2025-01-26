import sys
import math

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())


n, k, l, c, d, p, nl, np = gi()

drink = (k * l) / nl
lime = d * c
salt = p / np

print(math.floor(min(drink, lime, salt) / n))
