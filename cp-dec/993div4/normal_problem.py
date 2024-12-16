t = int(input()) 
for _ in range(t):
    n = input() 

    reversed_string = n[::-1]

    transformed_string = ""
    for char in reversed_string:
        if char == 'p':
            transformed_string += 'q'
        elif char == 'q':
            transformed_string += 'p'
        else:
            transformed_string += char  


    print(transformed_string)
