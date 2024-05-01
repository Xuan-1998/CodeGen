dp = [1]
for i in range(1, n):
    for j in range(i):
        if s[j] == '1':
            dp[i].append((i << 1) | 1)
        else:
            dp[i].extend(dp[j-1])
    if s[i-1] == '1':
        dp[i].append(2**i - 1)
    else:
        dp[i].extend(dp[i-1])
print(sorted(set([team for teams in dp[-1] for team in [bin(team)[3:]]])))
