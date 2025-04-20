import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    s = input().strip()
    
    if s == "abc":
        print("YES")
    elif s[0] == "b" and s[1] == "a":
        print("YES")
    elif s[0] == "c" and s[2] == "a":
        print("YES")
    elif s[1] == "c" and s[2] == "b":
        print("YES")
    else:
        print("NO")

        
