import sys


sys.stdout = open('cp-jan/output.txt', 'w')
sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())

for i in range(t):
    n, k = gi()
    if n % k == 0:
        print("YES")
        print(((str((n//k)) +" ") * k).strip())
