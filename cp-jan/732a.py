import sys
import math

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

k, r = gi()
c = 1
p = k

while True:
    if k % 10 == 0 or (k % 10) == r:
        break
    k = k + p 
    
    c += 1
    

print(c)