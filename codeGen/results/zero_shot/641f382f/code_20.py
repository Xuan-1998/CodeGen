from math import gcd
from sys import stdin

# Function to find the GCD of an array
def find_gcd(arr):
    result = arr[0]
    for element in arr[1:]:
        result = gcd(result, element)
    return result

# Read input from stdin
n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

# Base case: if there's already a 1 in the array, no operations are needed
if 1 in array:
    print(0)
else:
    # Check if it is possible to make all elements equal to 1
    if find_gcd(array) != 1:
        print(-1)
    else:
        # Find the minimum number of operations
        min_operations = n  # Initialize with the maximum possible value
        for i in range(n):
            current_gcd = array[i]
            for j in range(i+1, n):
                current_gcd = gcd(current_gcd, array[j])
                if current_gcd == 1:
                    min_operations = min(min_operations, j - i)
                    break
        print(n - min_operations)
