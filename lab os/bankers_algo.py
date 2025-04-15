def is_safe(processes, available, max_need, allocation):
    num_processes = len(processes)
    num_resources = len(available)
    
    # Calculate the need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    
    # Work and Finish arrays
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []
    
    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                # Allocate resources temporarily
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                safe_sequence.append(processes[i])
                found = True
                break
        
        if not found:
            return False, []
    
    return True, safe_sequence

# Example Usage
processes = [0, 1, 2, 3, 4]  # Process IDs
available = [3, 3, 2]  # Available resources of A, B, C
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Check if the system is in a safe state
safe, safe_sequence = is_safe(processes, available, max_need, allocation)
if safe:
    print("System is in a safe state.")
    print("Safe Sequence:", safe_sequence)
else:
    print("System is NOT in a safe state (Deadlock detected).")
