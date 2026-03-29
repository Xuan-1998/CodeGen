def max_earnings(booking_requests, tables):
    n = len(booking_requests)
    k = tables
    dp = [[0] * (sum(request[1] for request in booking_requests) + 1) for _ in range(k + 1)]
    
    for i in range(k + 1):
        for j in range(sum(request[1] for request in booking_requests) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                max_earn = 0
                for c, s, pi in booking_requests:
                    if pi <= j and c <= i:
                        earn = c * s + dp[max(0, i - c)][max(0, j - s)]
                        if earn > max_earn:
                            max_earn = earn
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], max_earn)
    
    total_earned = dp[k][sum(request[1] for request in booking_requests)]
    accepted_requests = 0
    remaining_tables = k
    remaining_money = sum(request[1] for request in booking_requests)
    for i, j in enumerate(reversed(range(sum(request[1] for request in booking_requests), 1))):
        if dp[k - i][j - sum(request[1] for request in booking_requests[:i+1])] != dp[k - i-1][j - sum(request[1] for request in booking_requests[:i])]:
            accepted_requests += 1
            remaining_tables -= min(k - i, len(booking_requests) - i)
            remaining_money -= sum(request[1] for request in booking_requests[i:i+remaining_tables])
    print(f"{accepted_requests} {total_earned}")
    
    table_assignments = []
    for i in range(n):
        if i < accepted_requests:
            table_assignments.append((i + 1, remaining_tables))
            remaining_tables -= 1
