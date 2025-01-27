import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().strip())

t = int(input())

for i in range(t):
    n, k = gi()  
    res = k + ((k-1) // (n-1))
    print(res)



