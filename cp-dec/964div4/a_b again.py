N = int(input())

if ((N > 0) and (N < 91)):
    for _ in range(N):
        a = list(map(int, input().split()))
        for num in a:
            if (num > 9 and num < 100):
                result = (num // 10) + (num % 10)
                print(result)
