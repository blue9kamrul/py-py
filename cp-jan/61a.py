import sys

# sys.stdout = open('cp-jan/output.txt', 'w')
# sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

a = input()
b = input()
res = []

for i in range(len(a) - 1):
    if a[i] == b[i]:
        res.append(0)
    else: 
        res.append(1)
    

res = "".join(map(str, res))
# if a[0] == b[0]:
#     print(0,res)
# else:
print(res)
