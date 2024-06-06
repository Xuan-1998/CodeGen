from math import gcd
from sys import stdin

def find_operations(arr):
    n = len(arr)
    
    # If there is already a 1 in the array, we can make the whole array equal to 1
    if 1 in arr:
        return n - 1
    
    # Check if it's possible to create a 1 by taking the GCD of any pair of adjacent elements
    for i in range(n):
        for j in range(i+1, n):
            if gcd(arr[i], arr[j]) == 1:
                return n - 1
    
    # If no 1 is found and it's not possible to create a 1, return -1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(find_operations(arr))
