
import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())

for i in range(n):
    l, r = gi()
    if l == 1 and r == 1:
        print(1)
        
    elif l == r:
        print(0)
    else:
        print(r-l)
        


        