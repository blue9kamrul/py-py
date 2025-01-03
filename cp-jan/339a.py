import sys

sys.stdout = open('cp-jan/output.txt', 'w')
sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split("+")))
gs = lambda: list(input().split())

n = gi()
n.sort()
result = "+".join(map(str, n))

print(result)