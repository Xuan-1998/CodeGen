MOD = 998244353

def read_ints():
    return list(map(int, input().split()))

def solve(N, sets):
    # Initialize dp table with 0's. We add one more to handle 1-based indexing.
    dp = [[0] * (200001) for _ in range(N + 1)]
    # Initialize the first set's values
    for x in sets[0]:
        dp[1][x] = 1
    
    # Build the dp table
    for i in range(2, N + 1):
        sum_previous = sum(dp[i-1]) % MOD  # Sum of all ways to form sequences with the previous set
        for x in sets[i-1]:
            # Number of ways to end with 'x' is the total ways minus the ways that ended with 'x' in the previous set
            dp[i][x] = (sum_previous - dp[i-1][x]) % MOD
    
    # Calculate the result as the sum of ways to end with any number in the last set
    result = sum(dp[N][x] for x in sets[N-1]) % MOD
    return result

# Read input
N = int(input())
sets = [read_ints()[1:] for _ in range(N)]

# Solve the problem and output the result
print(solve(N, sets))
