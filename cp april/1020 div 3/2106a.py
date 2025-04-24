import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    res = 0
    for j in range(n):
        if s[j] == '0':
            c = '1'
        else: 
            c = '0'
        if j == 0:
            ss =  c + s[j+1:]
        else:
            ss = s[0:j] + c + s[j+1:]
        # print(ss)
        for k in range(n):
            if ss[k] == '1':
                res += 1
    print(res)