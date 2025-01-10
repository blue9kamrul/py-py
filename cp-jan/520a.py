import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
s = input()
set = set()

for i in range(n):
    s = s.lower()
    if ord(s[i]) > 96 and ord(s[i]) < 123:
        set.add(s[i])      

if len(set) == 26:
    print("YES")
else:
    print("NO")