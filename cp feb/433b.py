import sys
 
sys.stdout = open('cp feb/output.txt', 'w')
sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))
 
 
n = int(input().strip())  
a = gi()  
m = int(input().strip())  
s = sorted(a)
for _ in range(m):
    b = gi()  
    left, right = b[1] - 1, b[2]  
    
    if b[0] == 1:
        print(sum(a[left:right]))  
    else:
        print(sum(s[left:right])) 