import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
a = gi()

mx = max(a)
mn = min(a)
c = 0
d = 0

# Move the maximum element to the front
for i in range(n):
    if a[i] == mx:
        c = i
        a.pop(i)  # Remove the element at index i
        a.insert(0, mx)  # Insert it at the front
        break

# Move the minimum element to the end
for i in range(len(a) - 1, -1, -1):  # Iterate from the last index
    if a[i] == mn:
        
        d = len(a) - 1 - i  # Calculate distance to the last position
        break

print(c + d)
