import sys
from tkinter import Y

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

y =int(input())
set = set()  

while True:
    y += 1
    y = str(y)
    for i in range(4):
        set.add(y[i])  
      
    if len(set) == 4:
        break
    set.clear()
    y = int(y)
    
print(y)