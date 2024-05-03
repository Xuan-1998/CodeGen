def max_distance(commands, n):
    dp = [0] * (len(commands) + 1)
    for i in range(len(commands)):
        if i >= n:
            dp[i + 1] = max(dp[i], dp[i - n] + (commands[i] == "F"))
        else:
            dp[i + 1] = dp[i]
    return dp[-1]

n = int(input())  # Number of commands to modify
commands = input()  # List of turtle commands

print(max_distance(commands, n))
