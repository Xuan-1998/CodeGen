import sys

def calculate_probability(N, P):
    # Convert P to a floating-point probability
    P = P / 100.0
    Q = 1 - P

    # Initialize the dp array with zeros and set dp[0] to 1
    dp = [0.0] * (N + 1)
    dp[0] = 1.0

    # Base cases
    if N >= 2:
        dp[2] = P
    if N >= 3:
        dp[3] = Q

    # Fill in the dp array using dynamic programming
    for i in range(4, N + 1):
        dp[i] = dp[i - 2] * P + dp[i - 3] * Q

    # Return the probability of reaching position N
    return '%.6f' % dp[N]

# Read the number of test cases
T = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(T):
    N, P = map(int, sys.stdin.readline().strip().split())
    print(calculate_probability(N, P))
