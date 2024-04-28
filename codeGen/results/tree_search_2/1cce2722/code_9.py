def max_points(sequence):
    n = len(sequence)
    dp = [[0, 0] for _ in range(n+1)]

    for i in range(2, n+1):
        if sequence[i-1] + dp[i-2][0] > dp[i-1][0]:
            dp[i][0] = sequence[i-1] + dp[i-2][0]
            dp[i][1] = 1
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]

    return dp[n][0]

# Read input from stdin
n = int(input())
sequence = [int(x) for x in input().split()]

print(max_points(sequence))
