import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))


n, m, a, b = gi()


normal = n * a


special = (n // m) * b + min((n % m) * a, b)


result = min(normal, special)

print(result)
