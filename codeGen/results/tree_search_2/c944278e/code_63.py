def winning_teams(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if (s >> i) & 1:
            dp[i] = max(dp[i-1], dp[i-1] + 2**i)
        else:
            dp[i] = dp[i-1]
    winning_teams = [i for i in range(n+1) if dp[i] == 2**n - 1]
    return sorted(winning_teams)

n = int(input())
s = bin(int(input()))[2:].zfill(n)
print(*winning_teams(n), sep='\n')
