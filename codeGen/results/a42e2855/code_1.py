# Function to calculate the probability of reaching position N
def calculate_probability(N, P):
    # Convert P to a fraction
    P /= 100.0
    Q = 1 - P

    # Initialize base cases
    dp = [0.0] * (max(N, 3) + 1)
    dp[0] = 1.0
    dp[2] = P

    # Use dynamic programming to fill in the dp array
    for i in range(3, N + 1):
        dp[i] = dp[i - 2] * P + dp[i - 3] * Q

    # Return the probability of reaching position N
    return dp[N]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, P = map(int, input().strip().split())
    probability = calculate_probability(N, P)
    # Print the probability with exactly 6 digits after the decimal point
    print(f"{probability:.6f}")
