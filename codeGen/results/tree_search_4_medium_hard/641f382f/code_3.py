import math
from sys import stdin

# Function to calculate gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the gcd of an array
def gcd_of_array(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return 1
    return current_gcd

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Check if there is already a 1 in the array
if 1 in arr:
    print(arr.index(1) + (n - 1 - arr[::-1].index(1)))
else:
    # Check if it is possible to create a 1
    if gcd_of_array(arr) == 1:
        print(n - 1)
    else:
        print(-1)
