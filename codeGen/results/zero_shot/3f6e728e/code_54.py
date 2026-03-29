import sys

# Read input
N, M, C = map(int, input().split())
U = list(map(int, input().split()))
L = list(map(int, input().split()))

# Sort radii in ascending order
U.sort()
L.sort()

dp = [0] * (C + 1)

# Initialize dp[0] to 1, because we can build an empty X-sequence
dp[0] = 1

# Code continues...
