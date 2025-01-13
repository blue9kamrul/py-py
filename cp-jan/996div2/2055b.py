import sys

# Open files for input and output
sys.stdin = open('cp-jan/input.txt', 'r')
sys.stdout = open('cp-jan/output.txt', 'w')

input = sys.stdin.readline

# Helper functions
gi = lambda: list(map(int, input().split()))

# Main logic
t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the size of the arrays
    a = gi()  # Read array `a`
    b = gi()  # Read array `b`
    
    # Initialize counter for mismatches
    c = 0
    
    for j in range(n):
        diff = a[j] - b[j]  # Calculate the difference between elements
        if n - c >= 1 :  # Check if the difference violates the condition
            c += 1

    # If exactly one element violates the condition, output "YES", otherwise "NO"
    if c == 0:
        print("YES")
    else:
        print("NO")

        