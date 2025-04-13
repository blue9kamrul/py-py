


def fcfs(processes):
    processes.sort(key = lambda x: x['at'])

    current_time = 0

    for process in processes:
        process['st'] = max(current_time,process['at'])

        process['ct'] = process['st'] + process['bt']
        current_time = process['ct']

        process['tat'] = process['ct'] - process['at']
        process['wt'] = process['tat'] - process['bt']

    return processes

def display(processes):
    print("pid\tat\tbt\tst\tct\ttat\twt")
    for p in processes:
        print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['st']}\t"
        f"{p['ct']}\t{p['tat']}\t{p['wt']}")
    avg_tat = sum(p['tat'] for p in processes)/len(processes)
    avg_wt = sum(p['wt'] for p in processes)/len(processes)
    print(avg_tat)
    print(avg_wt)
 



processes = [
    {'pid': 1, 'at': 0, 'bt': 2},
    {'pid': 2, 'at': 2, 'bt': 5},
    {'pid': 3, 'at': 3, 'bt': 6}
]

res = fcfs(processes)
display(res)