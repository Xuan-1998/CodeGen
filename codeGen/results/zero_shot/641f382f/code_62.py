from math import gcd
from functools import reduce

# Function to compute the GCD of all elements in the array
def gcd_of_all_elements(arr):
    return reduce(gcd, arr)

# Main function to find the minimum number of operations
def min_operations_to_make_all_elements_one(arr):
    # If there is an element which is 1, we can make all elements 1.
    if 1 in arr:
        return n - arr.count(1)
    
    # If GCD of all elements is not 1, it's impossible to make all elements 1.
    if gcd_of_all_elements(arr) != 1:
        return -1
    
    # Otherwise, we need to find the minimum number of operations
    min_operations = float('inf')
    
    for i in range(n):
        current_gcd = arr[i]
        operations = 0
        
        # Keep computing GCD with the next element until we reach 1 or the end of the array
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            operations += 1
            if current_gcd == 1:
                # Update minimum operations if we found a smaller number of operations
                min_operations = min(min_operations, operations)
                break
    
    return min_operations + (n - 1)  # Add (n - 1) operations to propagate the 1 to all elements

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(min_operations_to_make_all_elements_one(arr))
