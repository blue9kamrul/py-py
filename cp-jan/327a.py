import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

n = int(input())
arr = gi()
c = 0  

#using kadane's algo

ones_count = sum(arr)  
flipped = [1 if x == 0 else -1 for x in arr]

max_gain = float('-inf')
curr_sum = 0

for num in flipped:
    curr_sum = max(num, curr_sum + num)
    max_gain = max(max_gain, curr_sum)
    
if ones_count == n:
    print(n-1)
else:
    print(max_gain + ones_count)



