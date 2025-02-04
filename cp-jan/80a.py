import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n, m = gi()


next_prime = n + 1
while True:
    
    is_prime = True
    for i in range(2, int(next_prime ** 0.5) + 1):
        if next_prime % i == 0:
            is_prime = False
            break
    if is_prime:
        break
    next_prime += 1


if next_prime == m:
    print("YES")
else:
    print("NO")


