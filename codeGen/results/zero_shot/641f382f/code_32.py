import math
from sys import stdin

# Function to compute GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute GCD of an array
def gcd_array(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return 1
    return current_gcd

# Function to find the minimum number of operations
def min_operations(arr):
    # Compute the GCD of the entire array
    array_gcd = gcd_array(arr)
    
    # If the GCD is not 1, it's impossible to make all elements equal to 1
    if array_gcd != 1:
        return -1
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate through the array to find the first occurrence of 1
    for i in range(len(arr)):
        current_gcd = arr[i]
        # If we find a 1, we can stop as we can spread this 1 to the entire array
        if current_gcd == 1:
            # The number of operations is the distance from the current position to the start
            # plus the distance from the current position to the end of the array
            operations = i + (len(arr) - 1 - i)
            break
    
    return operations

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Output the minimum number of operations
print(min_operations(arr))
