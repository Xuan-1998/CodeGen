code
def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(min(i, n)+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][min(j-1, i)] + (commands[i-1] == 'F'), dp[i-1][j])

    return dp[m][n]

# Example usage
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
