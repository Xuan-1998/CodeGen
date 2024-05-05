import sys
from collections import defaultdict

# Get the maximum number of digits N from input
N = int(sys.stdin.readline().strip())

# Create a 1D DP table to store the cumulative sum modulo 10 for each digit position in A.
A_dp = [0] * (N + 1)
for i in range(N):
    # Read the ith digit of A and update the DP table
    A_digit = int(sys.stdin.readline().strip())
    for j in range(10):
        if ((j + A_digit) % 10 != 0):
            A_dp[i] += 1

# Create another 1D DP table to store the cumulative sum modulo 10 for each digit position in B.
B_dp = [0] * (N + 1)
for i in range(N):
    # Read the ith digit of B and update the DP table
    B_digit = int(sys.stdin.readline().strip())
    for j in range(10):
        if ((j + B_digit) % 10 != 0):
            B_dp[i] += 1

# Create a 2D DP table with dimensions N x N, where dp[i][j] represents the expected number of non-zero carries when adding A's i-th digit and B's j-th digit.
dp = [[0.0 for _ in range(N + 1)] for _ in range(N + 1)]

# Fill in the 2D DP table
for i in range(N):
    for j in range(N):
        # Calculate the expected number of non-zero carries as the sum of the product of the current digit of A and the cumulative sum modulo 10 up to that position in B, plus the cumulative sum modulo 10 up to that position in A.
        dp[i][j] = (float(A_dp[i]) / 10.0) * (float(B_dp[j]) / 10.0) + float(A_dp[i]) / 10.0 + float(B_dp[j]) / 10.0

# Calculate the final answer as the average of the values in the 2D DP table.
expected_carries = sum([sum(row) for row in dp]) / (N * N)

print("%.6f" % expected_carries)
