import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    a = []
    for j in range(n):
        a.append(s[j])
    a.sort()
    # print(a)
    ss = ["T", "i", "m", "u", "r"]
    # print(ss)
    ss.sort()
    if a == ss:
        print("YES")
    else:
        print("NO")