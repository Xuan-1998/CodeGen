from math import gcd

def min_operations_to_make_ones(n, array):
    # Check if there's already a 1 in the array
    if 1 in array:
        return 0
    
    # Check for adjacent pairs with GCD of 1
    for i in range(n - 1):
        if gcd(array[i], array[i + 1]) == 1:
            return 1  # We can propagate 1 to make all elements equal to 1
    
    # If no such pair is found, it's impossible to make all elements equal to 1
    return -1

# Read input from stdin
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(n, array))
