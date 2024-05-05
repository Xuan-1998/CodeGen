import sys

def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    last = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if s[i - 1] == 'R':
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + (s[i - 2] != 'G' and s[i - 3] != 'B'))
                last[i] = s[i - 1]
            elif s[i - 1] == 'G':
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + (s[i - 2] != 'R' and s[i - 3] != 'B'))
                last[i] = s[i - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + (s[i - 2] != 'G' and s[i - 3] != 'R'))
                last[i] = s[i - 1]
    
    print(k - dp[n][k])

solve()
