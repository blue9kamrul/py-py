import sys

sys.stdout = open('cp april/output.txt', 'w')
sys.stdin = open('cp april/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for i in range(t):
    p = input().strip()
    s = input().strip()
    lenp = len(p)
    pp = sorted(p)
    ss = sorted(s)
  
    i = j = 0
    while i < len(pp) and j < len(ss):
        if pp[i] == ss[j]:
            pp.pop(i)
            ss.pop(j)
        elif pp[i] < ss[j]:
            i += 1
        else:
            j += 1

    c = abs(len(ss) - lenp)
    
    if c % 2 == 0:
        print("NO")
    else:
        print("YES")
