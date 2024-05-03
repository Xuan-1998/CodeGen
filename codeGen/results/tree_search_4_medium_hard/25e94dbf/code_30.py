def max_distance(commands, n):
    m = len(commands)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if commands[i - 1] == 'T':
            dp[i] = max(dp[i - 1], dp[i - 2] + 1) if i >= 2 else 1
        elif commands[i - 1] == 'F':
            dp[i] = dp[i - 1] + 1

    return dp[n]

commands = input().strip()
n = int(input())
print(max_distance(list(commands), n))
