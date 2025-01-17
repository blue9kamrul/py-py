import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

n = int(input())  
levels = set()  


p = gi()
levels.update(p[1:])

q = gi()

levels.update(q[1:])


if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
