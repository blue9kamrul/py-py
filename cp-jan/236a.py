import sys

input = sys.stdin.readline

gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

n = input().strip()
ln = len(n)
s = set()

for i in range(ln):
  s.add(n[i])

if len(s) % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
