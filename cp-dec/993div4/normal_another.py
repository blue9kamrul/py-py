t = int(input())  

for _ in range(t):
    n = list(input())  
    reversed_list = n[::-1] 
    for i in range(len(reversed_list)):
        if reversed_list[i] == 'p':  
            reversed_list[i] = 'q'
        elif reversed_list[i] == 'q':  
            reversed_list[i] = 'p'

    print("".join(reversed_list))
