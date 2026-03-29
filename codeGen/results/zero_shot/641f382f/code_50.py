import math

def gcd(a, b):
    return math.gcd(a, b)

# Function to find the minimum number of operations
def min_operations_to_make_ones(n, arr):
    # Check if it's possible to make all elements 1
    array_gcd = arr[0]
    for num in arr:
        array_gcd = gcd(array_gcd, num)
        if array_gcd == 1:
            break

    if array_gcd > 1:
        return -1  # It's impossible to make all elements equal to 1

    # Find the minimum number of operations
    operations = 0
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            operations += 1

    return operations

# Reading input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output the result
print(min_operations_to_make_ones(n, arr))
