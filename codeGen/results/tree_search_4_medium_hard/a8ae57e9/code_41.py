def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        ci, pi = map(int, input().split())
        
        for j in range(k, -1, -1):
            if j >= ci:
                dp[i][j] = max(dp[i-1][j], pi + dp[i-1][j-ci])
            else:
                dp[i][j] = dp[i-1][j]
    
    accepted_requests = 0
    total_money_earned = 0
    
    for i in range(n, -1, -1):
        ci, pi = map(int, input().split())
        
        if j >= ci and pi + dp[i-1][j-ci] > dp[i-1][j]:
            accepted_requests += 1
            total_money_earned += pi
            j -= ci
    
    print(accepted_requests)
    print(total_money_earned)
    
    for _ in range(accepted_requests):
        request, table = map(int, input().split())
        print(f"{request} {table}")

if __name__ == "__main__":
    solve()
