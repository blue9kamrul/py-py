import sys

# sys.stdout = open('cp april/output.txt', 'w')
# sys.stdin = open('cp april/input.txt', 'r')



t = int(input())  
for _ in range(t):
    n = int(input())  
    s = input()  
    transitions = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            transitions += 1
    
    max_reduction = 0

    for i in range(1, n):
        if s[i] != s[i - 1]:  
            
            if i + 1 < n and s[i] != s[i + 1] and s[i - 1] == s[i + 1]:
                
                max_reduction = 2
                break  
            else:
                
                max_reduction = max(max_reduction, 1)

    
    final_transitions = transitions - max_reduction

    sa = list(set(s))
    if len(sa) == 1 and sa[0] == "0":
        cost = n
    else:
        cost = n + final_transitions + 1
    print(cost)
