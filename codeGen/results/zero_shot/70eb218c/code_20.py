import sys

def min_operations(n, x):
    # Convert integer to string
    x_str = str(x)
    
    # Calculate the difference in lengths
    diff_len = n - len(x_str)
    
    if diff_len < 0:
        return -1
    
    # Initialize count of operations
    ops_count = 0
    
    while diff_len > 0:
        # For each digit, replace it with x * y for some digit y (0-9)
        new_x = int(str(x_str) + '0' if diff_len % 2 == 1 else str(x_str) + '5')
        
        # Update the count of operations
        ops_count += 1
        
        # Update x and the difference in lengths
        x, x_str = new_x, str(new_x)
        diff_len -= 1
    
    return ops_count

# Read input from stdin
n, x = map(int, input().split())

print(min_operations(n, x))
