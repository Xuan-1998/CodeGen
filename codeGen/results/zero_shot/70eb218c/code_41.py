import math

def min_operations(n, x):
    # Convert x to string for easy manipulation
    x_str = str(x)
    
    # Calculate the current length of decimal representation of x
    curr_len = len(x_str)
    
    # If the current length is already equal to n, return 0
    if curr_len == n:
        return 0
    
    # Initialize the minimum number of operations
    min_ops = float('inf')
    
    # Iterate from 1 to 9 (possible digits in decimal representation)
    for digit in range(1, 10):
        # Convert x to an integer for multiplication
        int_x = int(x)
        
        # Calculate the length of decimal representation of int_x * digit
        new_len = len(str(int_x * digit))
        
        # If the new length is greater than or equal to n and less than or equal to curr_len
        if new_len >= n and (new_len == n or new_len > curr_len):
            # Calculate the number of operations required for this digit
            ops = curr_len - new_len
            
            # Update the minimum number of operations
            min_ops = min(min_ops, ops)
    
    # If it is impossible to make the length of decimal representation of x equal to n, return -1
    if min_ops == float('inf'):
        return -1
    
    # Return the minimum number of operations
    return min_ops

# Read input from standard input
n, x = map(int, input().split())

# Calculate and print the result
print(min_operations(n, x))
