import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n, k = gi()

participants = gi()
count = 0


for i in range(len(participants)):
    
    if participants[i] >= participants[k-1] and participants[i] > 0:
        count += 1
    
print(count)
