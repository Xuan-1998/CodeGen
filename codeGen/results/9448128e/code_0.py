print('MOD = 998244353

def count_sequences(sets):
    # Initialize dp table
    dp = [[0, 0] for _ in range(len(sets) + 1)]
    dp[0][0] = 1  # Base case

    for i in range(1, len(sets) + 1):
        set_size = len(sets[i - 1])
        # Number of sequences that can end with any number except the last of the previous set
        dp[i][0] = (dp[i - 1][0] * set_size + dp[i - 1][1] * (set_size - 1)) % MOD
        # Number of sequences that end with the same number as the last of the previous set
        # We can pick any number from the current set to be the last
        dp[i][1] = dp[i - 1][0]

    # The total number of sequences is the sum of sequences that end with any number and those that end with a specific number
    return (dp[len(sets)][0] + dp[len(sets)][1]) % MOD

# Read input from stdin
N = int(input())
sets = [list(map(int, input().split()))[1:] for _ in range(N)]

# Calculate and print the result
print(count_sequences(sets))')