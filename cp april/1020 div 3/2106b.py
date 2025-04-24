import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')
input = sys.stdin.readline


gi = lambda: list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n, x = gi()
    res = []

    if x == 0:
        for i in range(1, n):
            res.append(i)
        res.append(0)

    elif x == n:
        res = list(range(n))

    else:
        for i in range(x):
            res.append(i)

        for i in range(x + 1, n):
            res.append(i)
        res.append(x)

    print(*res)
