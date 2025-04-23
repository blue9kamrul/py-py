import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    s = input()
    ss = "codeforces"
    c = 0
    for j in range(10):
        if s[j] != ss[j]:
            c += 1
    print(c)