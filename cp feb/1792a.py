import sys
 
# sys.stdout = open('cp feb/output.txt', 'w')
# sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))


t = int(input())
s = list('codeforces')


for i in range(t):
    c = input().strip()
    
    if c in s:
        print("YES")
    else:
        print("NO")