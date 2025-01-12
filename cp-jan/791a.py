import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

a, b = gi()
count = 0
if a == b:
    count = 1
else:
    while a<=b:
        a = a * 3
        b = b * 2
        count += 1

print(count)