import math
import sys

# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the GCD of an array
def gcd_of_array(arr):
    array_gcd = arr[0]
    for num in arr[1:]:
        array_gcd = gcd(array_gcd, num)
        if array_gcd == 1:
            return 1
    return array_gcd

# Reading input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Main logic
if 1 in arr:  # If there's already a 1 in the array
    print(0)
else:
    array_gcd = gcd_of_array(arr)
    if array_gcd != 1:  # If it's not possible to get 1 as GCD
        print(-1)
    else:
        # Find minimum operations required
        min_operations = float('inf')
        for i in range(n):
            temp_gcd = arr[i]
            for j in range(i, -1, -1):  # Calculate prefix GCDs
                temp_gcd = gcd(temp_gcd, arr[j])
                if temp_gcd == 1:
                    min_operations = min(min_operations, i - j)
                    break
        print(min_operations)
