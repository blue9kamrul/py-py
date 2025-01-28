import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().strip()))
gs = lambda: list(input().strip())

n = gi()

for i in range(len(n)):

    if n[i] > 4:
        n[i] = 9 - n[i]
    
if n[0] == 0:
    n[0] = 9
print("".join(map(str,n)))