MOD = 998244353

# Function to read integers from a line
def read_ints():
    return list(map(int, input().split()))

# Read the number of sets
N = int(input())

# Read the sets
sets = [read_ints()[1:] for _ in range(N)]

# Initialize the DP array
dp = [{} for _ in range(N)]

# Base case: For the first set, all elements can be chosen as the last element
for num in sets[0]:
    dp[0][num] = 1

# Fill in the DP array
for i in range(1, N):
    for num in sets[i]:
        dp[i][num] = 0

        # Add the count from the previous set excluding the current number
        for prev_num in sets[i-1]:
            if prev_num != num:
                dp[i][num] += dp[i-1][prev_num]
                dp[i][num] %= MOD

# Sum up all the valid combinations for the last set
result = sum(dp[N-1].values()) % MOD

# Output the result
print(result)
