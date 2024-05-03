n_commands = int(input())  # Input: Number of commands that can be modified
commands = input()  # Input: String of turtle commands (T/F)

dp = [0] * (n_commands + 1)  # Initialize DP array with zeros

for i in range(1, n_commands + 1):
    if commands[i-1] == 'F':
        dp[i] = max(dp[i-1] + 1, dp[i-1])  # If last command is F, increment distance
    else:
        dp[i] = dp[i-1]  # If last command is T, keep previous distance

max_distance = dp[n_commands]
print(max_distance)  # Output: Maximum distance after executing n commands
