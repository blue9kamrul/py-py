import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

k  = int(input())
l  = int(input())
m  = int(input())
n  = int(input())
d  = int(input())

s = set(range(1,d+1))


for i in range(1,d+1):
    
    s.discard(i*k)
    s.discard(i*l)
    s.discard(i*m)
    s.discard(i*n)

print(d - len(s))


