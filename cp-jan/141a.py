import sys
from collections import Counter

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

g = input().strip()  
h = input().strip()
p = input().strip()

combined = g + h


count_combined = Counter(combined)
count_p = Counter(p)

if count_combined == count_p:
    print("YES")
else:
    print("NO")
