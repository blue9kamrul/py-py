# Function to implement FCFS Scheduling
def fcfs_scheduling(processes):
    # Sort processes by Arrival Time
    processes.sort(key=lambda x: x['arrival_time'])
    
    # Initialize times
    current_time = 0
    for process in processes:
        # Calculate start time
        process['start_time'] = max(current_time, process['arrival_time'])
        
        # Calculate completion time
        process['completion_time'] = process['start_time'] + process['burst_time']
        
        # Update current time
        current_time = process['completion_time']
        
        # Calculate Turnaround Time (TAT) and Waiting Time (WT)
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['burst_time']
    
    return processes

# Function to display results
def display_results(processes):
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t"
              f"{process['start_time']}\t{process['completion_time']}\t"
              f"{process['turnaround_time']}\t{process['waiting_time']}")
    
    # Calculate and display average TAT and WT
    avg_tat = sum(p['turnaround_time'] for p in processes) / len(processes)
    avg_wt = sum(p['waiting_time'] for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

# Example input
processes = [
    {'pid': 1, 'arrival_time': 0, 'burst_time': 5},
    {'pid': 2, 'arrival_time': 1, 'burst_time': 3},
    {'pid': 3, 'arrival_time': 2, 'burst_time': 8},
    {'pid': 4, 'arrival_time': 3, 'burst_time': 6}
]

# Run FCFS scheduling
scheduled_processes = fcfs_scheduling(processes)

# Display the results
display_results(scheduled_processes)
