import math
from sys import stdin

# Function to compute the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the GCD of an array
def gcd_of_array(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return 1  # Early exit if we find GCD is 1
    return current_gcd

# Main function to find the minimum number of operations
def min_operations_to_make_ones(arr):
    # Compute the GCD of the entire array
    array_gcd = gcd_of_array(arr)

    # If the GCD of the entire array is greater than 1, return -1
    if array_gcd > 1:
        return -1

    # Find the shortest subsequence with GCD 1
    n = len(arr)
    min_subseq_length = n
    for i in range(n):
        subseq_gcd = arr[i]
        for j in range(i + 1, n):
            subseq_gcd = gcd(subseq_gcd, arr[j])
            if subseq_gcd == 1:
                min_subseq_length = min(min_subseq_length, j - i + 1)
                break

    # The number of operations is the length of the array minus the length of the shortest subsequence
    return n - min_subseq_length

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Print the minimum number of operations to stdout
print(min_operations_to_make_ones(arr))
