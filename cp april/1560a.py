import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for _ in range(t):
    k = int(input())
    count = 0
    num = 1
    while True:
        if num % 3 != 0 and num % 10 != 3:
            count += 1
        if count == k:
            print(num)
            break
        num += 1
