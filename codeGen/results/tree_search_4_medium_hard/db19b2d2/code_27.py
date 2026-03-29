import sys

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]
    
    total_players = sum(s)
    department_interest_count = s[h-1]
    
    for i in range(h):
        dp[i][0] = 1.0
    
    for i in range(h, m+1):
        for k in range(n+1):
            if k == 0:
                dp[i][k] = 1.0
            elif k > 0 and s[i-1]:
                probability_player_from_interest_department = department_interest_count / sum(s[:i])
                dp[i][k] = max(dp[i-1][k], dp[i-1][k-1] + (s[i-1] > 0) * probability_player_from_interest_department)
    
    total_probability = 0.0
    for k in range(n+1):
        total_probability += dp[m][k]
    
    if n < department_interest_count:
        return -1
    
    return float(min([dp[m][i] / total_probability for i in range(n+1) if i >= n]))

print(calculate_probability())
