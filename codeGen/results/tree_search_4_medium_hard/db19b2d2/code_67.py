import sys

def basketball_team_prob():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[j - 1] >= i:
                dp[i][j] = max((s[j - 1] - i) / (n * (m - 1)) + dp[i][h], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
    
    if n > m:
        print(-1)
    else:
        print(dp[n][h])

if __name__ == "__main__":
    basketball_team_prob()
