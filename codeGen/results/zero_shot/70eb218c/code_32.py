import sys

def min_operations(n, x):
    current_len = len(str(x))
    diff = n - current_len
    
    if diff > 0:
        # Increase length by multiplying with a digit greater than 1
        operations = 0
        while diff > 0:
            max_digit = int('9' * (diff + 1))  # Calculate the maximum digit that can increase the length
            x *= max_digit
            current_len = len(str(x))
            diff -= (current_len - n)
            operations += 1
    elif diff < 0:
        # Decrease length by multiplying with a digit less than or equal to 1
        operations = 0
        while diff < 0:
            min_digit = int('1' * (-diff))  # Calculate the minimum digit that can decrease the length
            x *= min_digit
            current_len = len(str(x))
            diff += (n - current_len)
            operations -= 1
    else:
        return 0  # No operations needed
    
    return -1 if operations < 0 else operations

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Print the result to stdout
print(min_operations(n, x))
