import sys
from tkinter import Y

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n, k = gi()
y = gi()
for _ in range(k):
    for j in range(len(y)):
        
        if y[j] == 5:
            n -= 1
        y[j] += 1
print(n // 3)
        