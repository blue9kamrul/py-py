import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n,m = gi()


for i in range(n):
    
    if i % 2 == 0:
        print("#" * (m))
    elif i % 4 == 3:
        print("#" + "." * (m - 1))
    else: 
        print("." * (m - 1) + "#")
    
