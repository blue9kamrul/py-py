import sys

input = sys.stdin.readline

gi = lambda: list(map(int, input().split("+")))
gs = lambda: list(input().split())

n = gi()
n.sort()
result = "+".join(map(str, n))

print(result)