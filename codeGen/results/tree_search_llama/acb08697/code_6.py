def min_stones(n, s):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if s[i - 1] == '-':
            dp[i] = max(dp[i - 1] - 1, 0)
        else:
            dp[i] = max(dp[i - 1], 1)
    
    return dp[-1]

n = int(input())
s = input()
print(min_stones(n, s))
