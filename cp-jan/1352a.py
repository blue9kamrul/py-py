import sys


# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for _ in range(t):
    n = int(input())
    res = set()
    power = 1  

    while n > 0:
        digit = n % 10 
        if digit > 0:
            res.add(digit * power)  
        n //= 10  
        power *= 10  

    print(len(res))
    print(*sorted(res))  
