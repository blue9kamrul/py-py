# Fast Input/Output (if required for large inputs)
import sys
input = sys.stdin.read
############from sys import stdin, stdout  # noqa: E402

# Utility Functions
def read_int():
    """Reads a single integer."""
    return int(input().strip())

def read_ints():
    """Reads a list of integers."""
    return list(map(int, input().strip().split()))

def read_str():
    """Reads a single string."""
    return input().strip()

def read_strs():
    """Reads a list of strings."""
    return input().strip().split()

# Solve Function
def solve():
    """
    The main function to solve the problem.
    Write your logic here.
    """
    # Example: Sample Problem
########    n = read_int()  # Read single integer
    arr = read_ints()  # Read list of integers
    
    # Example logic: Find sum of array
    result = sum(arr)
    
    # Output the result
    print(result)

# Main Function
if __name__ == "__main__":
    """
    Ensures the code runs only when executed directly.
    Add test cases or logic to call the solve function.
    """
    # For competitive programming platforms
    solve()

    # Debugging / Local Testing
    # Use below block for testing locally with custom inputs
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    # solve()




# Key Elements in the Structure:
# Fast Input/Output:

# Use sys.stdin.read for handling large inputs efficiently.
# input() can be slower for competitive programming.
# Utility Functions:

# Modular functions like read_int, read_ints, etc., simplify repetitive input operations.
# Solve Function:

# Encapsulates the core logic of the problem. This modular approach helps in reusing code and debugging.
# Main Function:

# Calls solve() and handles the execution context.
# Local Testing:

# Includes commented code to read from and write to files for debugging during local testing.