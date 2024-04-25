import math
import sys

# Function to calculate the least common multiple
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().strip().split())
    
    # Calculate and print the minimum sum, which is the LCM of N and M
    print(lcm(N, M))

# Note: The lcm function uses the property that lcm(a, b) = abs(a * b) / gcd(a, b)
