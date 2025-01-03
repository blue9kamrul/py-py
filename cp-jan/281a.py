import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split("+")))
gs = lambda: list(input().split())

s =input()
s0 = s[0].upper()
print(s0 + s[1:])