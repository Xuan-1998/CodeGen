def calculate_probability(N, P):
    dp = [0.0] * (N + 1)
    dp[0] = 1.0  # The probability of being at the starting position is always 1

    # Handle base cases
    if N >= 2:
        dp[2] = P / 100.0
    if N >= 3:
        dp[3] = (100 - P) / 100.0

    # Fill in the rest of the dp array
    for i in range(4, N + 1):
        dp[i] = (dp[i - 2] * P / 100.0) + (dp[i - 3] * (100 - P) / 100.0)

    return dp[N]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, P = map(int, input().strip().split())
    probability = calculate_probability(N, P)
    print(f"{probability:.6f}")
