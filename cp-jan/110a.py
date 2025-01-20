import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = input()
r = 0
c = 0


for i in range(len(n)-1):
    if n[i] == "4" or n[i] == "7": 
        c += 1
    
if c == 7 or c == 4:
    print("YES")
else: 
    print("NO")



