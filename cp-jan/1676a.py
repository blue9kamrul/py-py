import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().strip()))
gs = lambda: list(input().strip())
t = int(input().strip())

for i in range(t):
    a = gi()
    
    if a[0]+a[1]+a[2] == a[3]+a[4]+a[5]:
        print("YES")
    else:
        print("NO")