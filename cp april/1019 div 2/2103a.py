import sys
import math
# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())
    a = gi()
    sa = list(set(a))
    print(len(sa))
    # res = []
    # for j in range(len(sa)-1):
    #     sa[j] = sa[j] * sa[j+1] // math.gcd(sa[j], sa[j+1])  
        