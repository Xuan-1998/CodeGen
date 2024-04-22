# Read the number of sets
N = int(input().strip())

# Initialize the dp array
dp = [[0, 0] for _ in range(N + 1)]
dp[1][1] = int(input().strip().split()[0])  # Read the size of the first set and assign it to dp[1][1]

# Process the rest of the sets
for i in range(2, N + 1):
    size = int(input().strip().split()[0])  # Read the size of the current set
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) * (size - 1) % MOD
    dp[i][1] = dp[i - 1][0] % MOD

# The answer is the sum of the two possibilities for the last set
answer = (dp[N][0] + dp[N][1]) % MOD
print(answer)