# Import the necessary libraries
import sys
from math import log2, ceil

# Initialize the variables
n, k = map(int, input().split())
total_and, total_xor = 0, 0
count = 0

# Iterate through each array element
for _ in range(n):
    # Read an integer from stdin and calculate its bitwise AND and XOR with the current total
    num = int(input())
    total_and |= num
    total_xor ^= num

# Calculate the bits of total AND and XOR
and_bits = ceil(log2(total_and + 1))
xor_bits = ceil(log2(total_xor + 1))

# Calculate the maximum possible bitwise AND value for any array
max_and = (1 << and_bits) - 1

# Calculate the maximum possible bitwise XOR value for any array
max_xor = (1 << xor_bits) - 1

# Iterate through each bit position from least significant to most significant
for i in range(and_bits):
    # Check if the ith bit of total AND is set
    if ((total_and >> i) & 1):
        # If it's set, we need at least this many arrays with their ith bit set for bitwise AND to be greater than or equal to bitwise XOR
        count += (max_xor >> i) + 1

# Print the result modulo 10^9+7
print(count % (10**9 + 7))
