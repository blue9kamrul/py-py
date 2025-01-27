import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

n, l = gi()

a = gi()
a.sort()

diff = 0

for i in range(1 , n, 1):
    if abs(a[i] - a[i-1]) > diff: 
        diff = abs(a[i] - a[i-1])

    
print(max((diff/2), a[0], l - a[-1]))