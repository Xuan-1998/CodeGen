def max_bitwise_or(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(i, n+1):
            if i == j:
                dp[i][j] = 0
            elif j - i == 1:
                dp[i][j] = int(s[i])
            else:
                max_or = 0
                for k in range(i+1, j):
                    or_val = dp[i][k] | int(s[k:j], 2)
                    if or_val > max_or:
                        max_or = or_val
                dp[i][j] = max_or

    return bin(max(dp[0][n-1]))[2:]

# Read input from standard input
n, s = map(int, input().split())
print(max_bitwise_or(bin(s)[2:]))
