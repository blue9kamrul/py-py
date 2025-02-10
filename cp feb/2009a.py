import sys
 
# sys.stdout = open('cp feb/output.txt', 'w')
# sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))


t = int(input())  # Number of test cases
for _ in range(t):
    a, b = gi()
    print(b - a)
