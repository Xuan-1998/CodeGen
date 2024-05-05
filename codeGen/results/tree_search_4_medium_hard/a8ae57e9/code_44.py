def max_earnings(booking_requests, k, table_capacity):
    n, m = len(booking_requests), sum(requests) // table_capacity
    dp = [[0] * (m + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, m + 1):
            if booking_requests[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - booking_requests[i - 1][0]] + booking_requests[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][j]

    table_assignments = []
    i, j = k, m
    while j > 0 and i > 0:
        if dp[i][j] != dp[i - 1][j]:
            table_assignments.append((i - 1, booking_requests[i - 2][0]))
            j -= booking_requests[i - 2][0]
        i -= 1

    return len(table_assignments), sum(booking_request[1] for booking_request in table_assignments)

