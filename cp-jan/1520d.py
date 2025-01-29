import sys
from collections import defaultdict

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = gi()
    
    freq = defaultdict(int)
    count = 0
    
    for i in range(n):
        diff = a[i] - i  
        count += freq[diff]  
        freq[diff] += 1  
    
    print(count)
