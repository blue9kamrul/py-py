import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

t = int(input())

for i in range(t):
    s = input().lower().strip()
    if s == "yes":
        print("YES")
    else:
        
        print("NO")