import math
from sys import stdin

# Function to read input and process the array
def min_operations_to_make_ones(n, array):
    # Check if any element is already 1
    if 1 in array:
        return n - 1

    # Initialize gcd with the first element
    gcd = array[0]

    # Compute the GCD of all elements
    for num in array[1:]:
        gcd = math.gcd(gcd, num)

    # If the GCD is not 1, it's not possible to make all elements 1
    if gcd != 1:
        return -1

    # Find the shortest subarray with GCD 1
    best_length = n
    for i in range(n):
        current_gcd = array[i]
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, array[j])
            if current_gcd == 1:
                best_length = min(best_length, j - i + 1)
                break

    # The minimum number of operations is n - length of the shortest subarray
    return n - best_length

# Read input from stdin
n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

# Calculate and print the result
print(min_operations_to_make_ones(n, array))
