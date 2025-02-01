import sys
import math

sys.stdout = open('cp-jan/output.txt', 'w')
sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())

for i in range(t):
    n, k = gi()
    if n % 2 == 0 and n - k > 1 :
        print("YES")
        print("2 " * (k - 1) + str((n - (2 * (k - 1)))))
    if n != 0 and n == k:
        print("YES")
        print("1 " * (k - 1) + str((n - (2 * (k - 1)))))
    else:
        print("NO")