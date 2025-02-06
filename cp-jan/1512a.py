import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = gi()
    c = 0
    for i in range(1,n,1):
        if a[0] != a[i]:
            c += 1
            idx = i
    if c == n-1 :
        print(1)
    else:
        print(idx+1)