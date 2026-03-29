import sys

def solve():
    n, k = map(int, input().split())
    dp = [[[0] * (k+1) for _ in range(n+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, min(i, n)+1):
            group_size, money_spent = map(int, input().split())
            if group_size <= i and money_spent <= dp[i-1][k][j-1]:
                dp[i][k][j] = max(dp[i][k][j], dp[i-1][k][j-1] + money_spent)
            else:
                dp[i][k][j] = dp[i][k][j-1]

    accepted_requests = sum(1 for i in range(k, -1, -1) if dp[i][k][n])
    total_money_earned = dp[k][k][n]
    
    print(f"{accepted_requests} {total_money_earned}")
    
    for i in range(n, 0, -1):
        if dp[k][k][i]:
            group_size, money_spent = map(int, input().split())
            table_index = k
            while table_index > 0 and dp[table_index-1][k][i-1] >= money_spent:
                table_index -= 1
            print(f"{i} {table_index}")
