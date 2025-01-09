import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())

s = 'I hate '
s2 = 'it'
s0 = 'that I love '
s1 = 'that I hate '
res = ''
if n == 1:
    print(s + s2)
else:
    for i in range(n-1):
        if i % 2 == 0:
            s = s + s0
        if i % 2 != 0:
            s = s + s1
    print(s + s2) 
