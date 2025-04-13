def round_robin(processes, quantum):

    current_time = 0
    queue = processes.copy()  # Copy of the process list to avoid modifying the original
    completed_processes = []
    
    # Adding additional fields for tracking remaining time
    for process in queue:
        process['remaining_time'] = process['burst_time']
    
    while queue:
        # finding which processes arrived at current time
        for process in queue[:]:  # Iterate over a shallow copy since the list will be modified
            if process['remaining_time'] > 0:
                # Calculating how much remaining time left
                if process['remaining_time'] > quantum:
                    current_time += quantum
                    process['remaining_time'] -= quantum
                else:
                    current_time += process['remaining_time']
                    process['remaining_time'] = 0
                    process['completion_time'] = current_time
                    process['turnaround_time'] = current_time - process['arrival_time']
                    process['waiting_time'] = process['turnaround_time'] - process['burst_time']
                    completed_processes.append(process)
                    queue.remove(process)  # Remove process from the queue once complete
    
    return completed_processes

def display_results(processes):
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t"
              f"{process['completion_time']}\t{process['turnaround_time']}\t{process['waiting_time']}")
    
    # Calculate and display average TAT and WT
    avg_tat = sum(p['turnaround_time'] for p in processes) / len(processes)
    avg_wt = sum(p['waiting_time'] for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

# Example Input
processes = [
    {'pid': 1, 'arrival_time': 0, 'burst_time': 10},
    {'pid': 2, 'arrival_time': 1, 'burst_time': 5},
    {'pid': 3, 'arrival_time': 2, 'burst_time': 8},
    {'pid': 4, 'arrival_time': 3, 'burst_time': 6}
]
quantum = 3

# Run Round Robin Scheduling
scheduled_processes = round_robin(processes, quantum)

# Display the results
display_results(scheduled_processes)
