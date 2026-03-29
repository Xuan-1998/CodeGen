def min_operations(n, x):
    # Initialize dp table with -1 values
    dp = [[-1 for _ in range(10)] for _ in range(n + 1)]

    # Base case: if length is already 0, it's impossible to make it equal to i
    for j in range(10):
        dp[0][j] = -1

    # Fill up the dp table using state transitions
    for i in range(1, n + 1):
        for j in range(10):
            if i == 1:
                dp[i][j] = 0
            else:
                for k in range(10):
                    dp[i][j] = min(dp[i - 1][k] + (j != k), dp[i][j])

    # Find the last digit of x and return the minimum number of operations
    d = int(str(x)[-1])
    if dp[n][d] == -1:
        return -1
    else:
        return dp[n][d]

# Read input from stdin
n, x = map(int, input().split())

# Print output to stdout
print(min_operations(n, x))
