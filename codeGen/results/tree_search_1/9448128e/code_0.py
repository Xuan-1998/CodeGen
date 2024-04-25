MOD = 998244353

def read_ints():
    return list(map(int, input().split()))

# Read the number of sets
N = int(input())

# Initialize the DP table
dp = [{} for _ in range(N)]

# Read the first set and initialize the base case
first_set = read_ints()[1:]
for j in first_set:
    dp[0][j] = 1

# Process the remaining sets
for i in range(1, N):
    current_set = read_ints()[1:]
    for element in current_set:
        dp[i][element] = sum(dp[i-1].get(k, 0) for k in dp[i-1] if k != element) % MOD

# Calculate the final answer
answer = sum(dp[N-1].values()) % MOD

# Print the answer
print(answer)
