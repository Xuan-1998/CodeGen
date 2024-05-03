def max_distance(commands, n):
    dp = [0] * (n + 1)
    for i in range(1, len(commands) + 1):
        if commands[i - 1] == "F":
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] - 1)
    return dp[-1]

n = int(input())  # read the number of modifications allowed
commands = input().strip()  # read the turtle command sequence

print(max_distance(commands, n))  # output the maximum distance traveled
