import sys

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = gi()

print((n[0] * n[1]) // 2)
