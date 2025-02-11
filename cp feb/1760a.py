import sys
 
# sys.stdout = open('cp feb/output.txt', 'w')
# sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))

t = int(input())

for i in range(t):
    a = gi()
    a.remove(max(a))
    a.remove(min(a))
    print(a[0])

