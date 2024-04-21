def calculate_probability(N, P):
    # Since we only need the last 3 probabilities to calculate the current one,
    # we can use just a small list with 3 elements and rotate it accordingly.
    dp = [0.0, 0.0, 1.0]  # Initial probabilities: dp[2] is the starting point with probability 1

    for i in range(3, N + 1):
        # Calculate the probability of reaching position i
        dp_new = (dp[(i - 2) % 3] * (P / 100)) + (dp[(i - 3) % 3] * ((100 - P) / 100))
        dp[i % 3] = dp_new  # Update the dp list for the new position

    return dp[N % 3]  # The final probability is at position N % 3

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, P = map(int, input().split())
    probability = calculate_probability(N, P)
    print(f"{probability:.6f}")  # Print the probability with 6 decimal places
