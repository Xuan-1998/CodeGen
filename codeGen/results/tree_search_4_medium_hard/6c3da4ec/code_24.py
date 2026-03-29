def maxOrValue(n, s):
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Fill up the DP table
    for i in range(1, n+1):
        for j in range(i, n+1):
            if s[i-1] == '0':
                dp[j][i] = max(dp[j][i-1], dp[j-1][i])
            else:
                dp[j][i] = max(dp[j-1][i-1], dp[j][i-1]) | (1 << (j-1))

    # Return the maximum value stored in any cell
    return format(max(max(row) for row in dp), 'b').count('1')

# Example usage:
n = int(input())
s = input()
print(maxOrValue(n, s))
