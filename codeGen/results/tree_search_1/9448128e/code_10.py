MOD = 998244353

# Read the number of sets
N = int(input())

# Initialize the dp list with empty dictionaries to store the count for each element
dp = [{} for _ in range(N+1)]

# Read the first set and initialize the dp values
first_set_size, *first_set = map(int, input().split())
for j in first_set:
    dp[1][j] = 1

# Process the rest of the sets
for i in range(2, N+1):
    current_set_size, *current_set = map(int, input().split())
    for j in current_set:
        dp[i][j] = 0
        # Transition from the previous set
        for k in dp[i-1]:
            if k != j:
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD

# Sum up the ways to end with each element in the last set
result = sum(dp[N].values()) % MOD

# Output the result
print(result)
