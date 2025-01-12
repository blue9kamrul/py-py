import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n , k = gi()
extra = 240 - k
count = 0
sum = 5

for i in range(n):
    if extra < 5:
        break
    elif extra >= sum:
        count += 1
        extra = extra - (i + 1) * 5
        sum += 5
        
print(count)