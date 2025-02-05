import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = gi()
    
    a.sort() 

    possible = True
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) > 1:
            possible = False
            break

    print("YES" if possible else "NO")
