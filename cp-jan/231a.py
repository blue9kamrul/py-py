n = int(input())
solved = 0
for i in range(n):
    p, v, t = map(int, input().split())
    if (p and v) or (p and t) or (v and t):
        solved += 1

print(solved)