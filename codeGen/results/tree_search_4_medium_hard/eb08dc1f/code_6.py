def block_count(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]

    # Initialize base case: count of blocks ending at each digit position with length 1 is 1
    for i in range(10):
        dp[i][1] = 1

    # Fill up the DP table
    for j in range(2, n + 1):
        for i in range(10):
            # If the current digit is the same as the previous one, it belongs to the same block
            if j > 1:
                dp[i][j] = (dp[i][j - 1] + dp[i][j]) % MOD
            else:
                dp[i][j] = 1

    # Count the number of blocks ending at each digit position with length n
    total_blocks = sum(dp[i][n] for i in range(10))
    return str(total_blocks)

# Read input and print output
n = int(input())
print(block_count(n))
