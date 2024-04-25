MOD = 998244353

def read_ints():
    return list(map(int, input().split()))

# Read the number of sets
N = int(input())

# Initialize our dp array with two dictionaries
dp = [{} for _ in range(2)]

# Read the first set and initialize the first dictionary
first_set = read_ints()[1:]  # Skip the size
for x in first_set:
    dp[0][x] = 1

# Process the rest of the sets
for i in range(1, N):
    current_set = read_ints()[1:]  # Skip the size
    # Clear the dictionary for the current set
    dp[i % 2].clear()
    # Calculate the sum of all counts from the previous set
    total_prev = sum(dp[(i - 1) % 2].values()) % MOD
    for x in current_set:
        # If x was used to end the previous sequence, we can't use it again
        # Otherwise, we can use x, and the number of ways to do that is the total number of ways
        # to form sequences from the previous sets minus the number of ways that ended with x
        dp[i % 2][x] = (total_prev - dp[(i - 1) % 2].get(x, 0)) % MOD

# Calculate the sum of all counts for the last set
result = sum(dp[(N - 1) % 2].values()) % MOD

# Output the result
print(result)
