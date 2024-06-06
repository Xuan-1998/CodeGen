from math import gcd
from sys import stdin

def find_min_operations(n, array):
    # Check if there is already a '1' in the array
    if 1 in array:
        return n - array.count(1)
    
    # Compute the GCD of the entire array
    overall_gcd = array[0]
    for num in array[1:]:
        overall_gcd = gcd(overall_gcd, num)
        if overall_gcd == 1:
            break
    
    # If the GCD is not 1, we cannot make all elements equal to 1
    if overall_gcd != 1:
        return -1
    
    # Find the minimum number of operations required
    min_operations = float('inf')
    for i in range(n):
        current_gcd = array[i]
        operations = 0
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, array[j])
            operations += 1
            if current_gcd == 1:
                min_operations = min(min_operations, operations + i + (n - j - 1))
                break
    
    return min_operations

# Read input from stdin
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))

# Compute and print the result
print(find_min_operations(n, array))
