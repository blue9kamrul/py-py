import sys
sys.stdout = open('cp-dec/output.txt', 'w')
sys.stdin = open('cp-dec/input.txt', 'r')


stdin = sys.stdin.read().splitlines()
del stdin[0]
c = 0
p = 0
for v in stdin:
    o, i = map(int, v.split())
    p += i - o
    c = max(c, p)
print(str(c))