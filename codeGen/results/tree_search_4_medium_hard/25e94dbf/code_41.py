def max_distance_reachable(commands, n):
    dp = [[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(len(commands)+1)]
    
    for i in range(len(commands)+1):
        for j in range(min(i, n)+1):
            if i == 0:
                continue
            elif j > 0:
                dp[i][j]['T' if commands[i-1] == 'F' else 'F'] = max(
                    dp[i-1][j-1]['T' if commands[i-1] == 'F' else 'F'],
                    dp[i-1][j-1]['T' if commands[i-1] == 'T' else 'F']
                )
            else:
                dp[i][j][commands[i-1]] = 1 + dp[i-1][j][commands[i-1]]
    
    return dp[-1][-1]['F']

# Test the function
commands = list(input())
n = int(input())
print(max_distance_reachable(commands, n))
