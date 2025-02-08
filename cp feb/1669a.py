import sys
 
# sys.stdout = open('cp feb/output.txt', 'w')
# sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))
 

t = int(input())

for i in range(t):
    n = int(input())
    if n>=1900:
        print("Division 1")
    elif n>=1600 and n<1900:
        print("Division 2")
    elif n>=1400 and n<1600:
        print("Division 3")
    else:
        print("Division 4")