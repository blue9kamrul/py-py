k, n, w = map(int, input().split())

sum = 0
for i in range(w):
    sum = sum + (i + 1) * k

if n > sum:
    print("0")
else:
    print(sum - n)
