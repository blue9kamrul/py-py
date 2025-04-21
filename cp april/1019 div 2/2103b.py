import sys

sys.stdout = open('cp april/output.txt', 'w')
sys.stdin = open('cp april/input.txt', 'r')



t = int(input())  
for _ in range(t):
    n = int(input())  
    s = input()  

    # Step 1: Count initial number of transitions (0 -> 1 or 1 -> 0)
    transitions = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            transitions += 1
    
    # Step 2: Try reversing substrings and check transitions
    min_transitions = transitions  # We will start with the original transition count

    # Test the effect of reversing all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            reversed_s = s[:i] + s[i:j][::-1] + s[j:]
            # Recompute transitions after reversal
            new_transitions = 0
            for k in range(1, n):
                if reversed_s[k] != reversed_s[k - 1]:
                    new_transitions += 1
            min_transitions = min(min_transitions, new_transitions)
    
    # Step 3: Calculate the final cost
    if s[0] == "0":
        cost = n + min_transitions 
    else:
        cost = n + min_transitions + 1

    print(cost)
