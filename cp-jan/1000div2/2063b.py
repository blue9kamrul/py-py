import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))

t = int(input())  

for _ in range(t):
   
    n, l, r = gi()
    a = gi()  
    
    
    l -= 1
    r -= 1

    
    inside = a[l:r+1]
    outside = a[:l] + a[r+1:]
    
    
    inside.sort(reverse=True)
    outside.sort()

    
    range_sum = sum(inside)

    
    for i in range(min(len(inside), len(outside))):
        if inside[i] > outside[i]:
            range_sum += outside[i] - inside[i]
        else:
            break

    
    print(range_sum)

    
        
