import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

n = gi()
mx = max(n)
new = []

for i in range(len(n)):
    if mx - n[i] != 0:
        new.append(mx - n[i])
print(" ".join(map(str,new)))