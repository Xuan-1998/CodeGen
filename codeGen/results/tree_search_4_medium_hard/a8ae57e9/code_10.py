def max_earned(k, pi, requests):
    dp = [[0] * (pi + 1) for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(1, pi + 1):
            if requests[0][0] <= i and requests[0][1] >= j:
                dp[i][j] = max(dp[i-1][j], dp[k][pi-j])
                requests.pop(0)
            else:
                dp[i][j] = dp[i-1][j]
                
    total_earned = 0
    for request in requests:
        if request[0] <= k and request[1] >= dp[k][request[1]]:
            total_earned += request[1]
    
    return total_earned, len(requests), [(i+1) for i, _ in enumerate(requests)]
