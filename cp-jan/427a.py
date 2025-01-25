import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

n = int(input())
t = gi()

c = 0  
h = 0  

for i in range(n):
    if t[i] == -1:  
        if h > 0:  
            h -= 1
        else:  
            c += 1
    else:  
        h += t[i]

print(c)

