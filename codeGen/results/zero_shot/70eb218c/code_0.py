def min_operations(n, x):
    # Convert x to a string to easily access its digits
    x_str = str(x)
    
    # Calculate the current length of x's decimal representation
    curr_len = len(x_str)
    
    # If the current length is already equal to n, return 0
    if curr_len == n:
        return 0
    
    # Initialize the minimum number of operations
    min_ops = -1
    
    # Iterate over each digit in x's decimal representation
    for i in range(curr_len):
        # Calculate the new length if we remove this digit
        new_len = curr_len - 1
        
        # If removing this digit makes the length equal to n, update min_ops
        if new_len == n:
            min_ops = 0
            break
        
        # Iterate over each possible value for the next digit (0-9)
        for y in range(10):
            # Calculate the new value of x if we replace this digit with y
            new_x = int(x_str[:i] + str(y) + x_str[i+1:])
            
            # Calculate the length of the new x's decimal representation
            new_len = len(str(new_x))
            
            # If the new length is equal to n, update min_ops and break
            if new_len == n:
                min_ops = 0
                break
        
        # If we've found a way to make the length equal to n, break out of the loop
        if min_ops != -1:
            break
    
    return min_ops

# Read input from stdin
n, x = map(int, input().split())

# Print the result to stdout
print(min_operations(n, x))
