import sys
 
sys.stdout = open('cp feb/output.txt', 'w')
sys.stdin = open('cp feb/input.txt', 'r')
 
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))



t = int(input().strip())
results = []

for _ in range(t):
    x, y = gi()
    
    # Construct an n where S(n) = x
    if x == 1 and y == 2:  # Edge case (Only 1 → 2 happens with 10)
        results.append("YES")
        continue

    for nine_count in range(1, 100):  # Use up to 100 nines
        n = int("9" * nine_count)  # A number like 9, 99, 999...
        s_n = sum(map(int, str(n)))
        
        if s_n > x:
            break  # Stop if we exceed the required sum
        
        if s_n == x:
            n_plus_1 = n + 1
            s_n1 = sum(map(int, str(n_plus_1)))
            
            if s_n1 == y:
                results.append("YES")
                break
    else:
        results.append("NO")

print("\n".join(results))