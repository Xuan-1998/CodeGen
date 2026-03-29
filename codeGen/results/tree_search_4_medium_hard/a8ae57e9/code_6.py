def max_earnings(n, groups, tables):
    k = len(tables)
    dp = [[[0, 0, [0]*k] for _ in range(max(groups)+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, max(groups)+1):
            for k_table in range(k):
                if groups[i-1][1] <= tables[k_table]:
                    dp[i][j][k_table][0] = max(dp[i-1][j][k_table][0], dp[i-1][j-1][k_table-1][0] + groups[i-1][1])
                    break
                else:
                    dp[i][j][k_table][0] = dp[i-1][j][k_table][0]
    
    max_earnings = 0
    for k_table in range(k):
        max_earnings = max(max_earnings, dp[n][max(groups)][k_table][0])
    
    accepted_requests = []
    remaining_capacities = [[tables[i] for _ in range(len(tables))] for i in range(n+1)]
    for i in range(n-1, -1, -1):
        if max_earnings == dp[i][max(groups)][k]:
            accepted_requests.append((i, k))
            remaining_capacities[i][k] -= groups[i][0]
    
    print(f"{len(accepted_requests)} {max_earnings}")
    for request in accepted_requests:
        print(*request)
