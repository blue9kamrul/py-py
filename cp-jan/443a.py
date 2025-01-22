
import sys

sys.stdout = open('cp-jan/output.txt', 'w')
sys.stdin = open('cp-jan/input.txt', 'r')

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = input().rstrip()
s = set()

for i in range(1, len(n)-1, 3):
    print(i)
    s.add(n[i])

print(len(s))