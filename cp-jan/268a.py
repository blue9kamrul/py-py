import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())
h = []
a = []
c = 0

for i in range(t):
    s = gi()
    h.append(s[0])
    a.append(s[1])
    

for i in range(t):
    for j in range(t):
        if h[i] == a[j]:
            c += 1
        
print(c)         
