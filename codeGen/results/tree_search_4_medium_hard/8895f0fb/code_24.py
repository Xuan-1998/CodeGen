import sys
from collections import defaultdict

# Initialize the DP table
dp = [[0] * 10 for _ in range(10)]

for i in range(1, 10):
    dp[i][i] = 1.0  # Each digit carries itself with probability 1.0
    if i < 5:
        dp[0][i] = 1.0  # A carry occurs when the last digit of A is 0 and the last digit of B is i

for i in range(10):
    for j in range(i+1, 10):
        dp[i][j] = 0.5  # Each pair of digits carries with probability 0.5
        if i < 5:
            dp[0][j] += dp[i][j]

# Initialize the result for each test case
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())

    # Calculate the expected number of non-zero carries for all pairs of N-digit numbers
    total_pairs = 10 ** (N - 1)
    total_carries = sum(sum(dp[i][j] for j in range(10)) for i in range(10))
    result = total_carries / total_pairs

    print(result)
