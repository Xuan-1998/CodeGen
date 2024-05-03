def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for k in range(min(i, n) + 1):
            if commands[i - 1] == 'F':
                dp[i][k] = dp[i - 1][k] + 1
            elif k > 0:
                dp[i][k] = max(dp[i - 1][k - 1] + (commands[i - 1] == 'F'), dp[i - 1][k])
            else:
                dp[i][k] = dp[i - 1][k]

    return dp[m][n]


if __name__ == "__main__":
    commands = input().strip()
    n = int(input())
    print(max_distance(commands, n))
