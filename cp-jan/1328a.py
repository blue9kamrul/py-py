
import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    remainder = a % b
    if remainder == 0:
        results.append(0)
    else:
        results.append(b - remainder)

print("\n".join(map(str, results)))