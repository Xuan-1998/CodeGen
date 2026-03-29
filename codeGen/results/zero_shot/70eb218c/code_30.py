import sys

def min_operations(n, x):
    # Calculate the current length of x
    curr_length = len(str(x))

    if curr_length == n:
        return 0
    
    # If the current length is less than n, we need to make it longer
    if curr_length < n:
        # Find a digit y such that x * y has more digits than x
        for y in range(10):
            next_length = len(str(x * y))
            if next_length > curr_length and next_length == n:
                return 1
    
    # If the current length is greater than or equal to n, we need to make it shorter
    else:
        # Find a digit y such that x / y has fewer digits than x
        for y in range(10**n, 0, -1):
            if str(x // y).count('0') == len(str(x // y)) - 1:
                return -1
    
    return -1

# Read input from stdin
n, x = map(int, input().split())

# Calculate and print the minimum number of operations
print(min_operations(n, x))
