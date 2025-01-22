import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = int(input())
r = n
c = d = e = f = g = 0

if r // 100 > 0: 
    c = r // 100 
    r = r % 100
        

if  r // 20 > 0:
    d = (r // 20)
    r = r % 20
    
         
if  r // 10 > 0:
    e = (r // 10)
    r = r % 10
    
        
if  r // 5 > 0:
    f = (r // 5)
    r = r % 5
    
g = r

        
print(int(c+d+e+f+g))
