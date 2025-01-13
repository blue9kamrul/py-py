import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n, h = gi()

heights = gi()
count = 0
# print(heights)


for i in range(n ):
    if heights[i] <= h:
        count += 1
        # print(int(heights[i]))
    else:
        count += 2
        # print(int(heights[i]))
    
print(count)
        
    