
def sjf(processes):
    processes.sort(key = lambda x: (x['at'], x['bt']))

    current_time = 0
    done_p = [  ]

    while processes:
        available = [p for p in processes if p['at']<= current_time]
        if available:
            next = min(available, key = lambda x: x['bt'])
            processes.remove(next)

            next['st'] = max(current_time,next['at'])
            next['ct'] = next['st'] + next['bt']
            current_time = next['ct']

            next['tat'] = next['ct'] - next['at']
            next['wt'] = next['tat'] - next['bt']

            done_p.append(next)
        else:
            current_time = processes[0]['at']
    return done_p

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
    {'pid': 1, 'at': 0, 'bt':2},
    {'pid': 2, 'at': 2, 'bt': 5},
    {'pid': 3, 'at': 3, 'bt': 6}
] 

res = sjf(processes)
display(res)
