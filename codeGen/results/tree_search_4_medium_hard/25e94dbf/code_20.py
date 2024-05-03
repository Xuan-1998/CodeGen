===BEGIN CODE===
def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(min(i, n) + 1):
            if i <= j:
                dp[i][j] = i
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][min(j - 1, n)] + 1)

    return dp[m][n]

if __name__ == "__main__":
    commands = input().strip()
    n = int(input())
    print(max_distance([cmd for cmd in commands if cmd in ['T', 'F']], n))
===END CODE===
