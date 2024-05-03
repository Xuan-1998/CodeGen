def max_distance(commands, n):
    dp = [[0] * (n + 1) for _ in range(len(commands) + 1)]
    
    forward_distance = 0
    backward_distance = 0
    
    for i in range(1, len(commands) + 1):
        if commands[i - 1] == 'F':
            forward_distance += 1
            dp[i][n] = max(dp[i-1][n], forward_distance)
        elif commands[i - 1] == 'T':
            backward_distance = min(backward_distance + forward_distance, 0)
            dp[i][n] = max(dp[i-1][n], backward_distance)
    
    return dp[-1][-1]

if __name__ == "__main__":
    n_commands, n_modifications = map(int, input().split())
    commands = list(input())
    print(max_distance(commands, n_modifications))
