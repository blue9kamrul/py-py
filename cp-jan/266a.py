import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
s = input()
count = 0

for i in range(n-1):
    if s[i] == s[i+1]:
        count+=1

print(count)
