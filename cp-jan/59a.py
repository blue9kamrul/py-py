import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

s =input()
l = 0
u = 0

for i in range(len(s)):
    if s[i].islower():
        l+=1
    elif s[i].isupper(): 
        u+=1

if l>u or l==u:
    s = s.lower()
else:
    s = s.upper()

print(s)