def solve(n, s):
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    
    # Base case: Each team has an equal chance of winning in the first round
    for j in range(1 << n):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for j in range(1 << n):
            # Update state transition as the maximum of dp[i-1][team]
            # for teams that can beat team j in round i
            for k in range(1 << n):
                if s[i - 1] == '0' and (j & k) != k:  # Team j can win if k beats j
                    dp[i][j] = max(dp[i][j], dp[i - 1][k])
    
    # Find all winning teams in ascending order
    winning_teams = []
    for j in range(1 << n):
        if dp[n][j]:
            winning_teams.append(bin(j)[2:].zfill(n))
    
    return sorted(winning_teams)

# Read input from stdin and print output to stdout
n = int(input())
s = input()
print(solve(n, s))
