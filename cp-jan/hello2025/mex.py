def maximize_mex_sum(t, test_cases):
    results = []
    for n, m in test_cases:
        if n == 1 or m == 1:
            # Special case: Single row or single column
            max_mex_sum = 2
        else:
            # General case
            max_mex_sum = n + m - 2
        results.append(max_mex_sum)
    return results

# Input reading
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    test_cases = []
    for _ in range(t):
        n, m = map(int, input().split())
        test_cases.append((n, m))

    # Solve the problem
    results = maximize_mex_sum(t, test_cases)

    # Output the results
    for res in results:
        print(res)
