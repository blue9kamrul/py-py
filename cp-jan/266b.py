import sys


sys.stdout = open('cp-jan/output.txt', 'w')
sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

n, t = gi()
s = gs()

for i in range(t):
    j = 0
    while j < n-1:
        if s[j] == "B" and s[j+1] == "G":
            s[j],s[j+1] = s[j+1],s[j]
            j += 1
        j += 1

print("".join(s))