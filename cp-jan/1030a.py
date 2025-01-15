import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
o = gi()
h = 0

for i in range(n): 
    if o[i] == 1:
        h += 1
        break

if h  == 1:
    print("HARD")
else:
    print("EASY")