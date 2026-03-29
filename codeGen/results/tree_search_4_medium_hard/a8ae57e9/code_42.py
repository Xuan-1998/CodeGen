def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    tables = list(map(int, input().split()))
    requests = []
    for _ in range(n):
        group_size, money = map(int, input().split())
        requests.append((group_size, money))

    requests.sort(reverse=True)

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if requests[i - 1][0] <= tables[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + requests[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][j]

    accepted_requests = 0
    total_money = 0
    table_assignments = []
    for i in range(n, 0, -1):
        if dp[i][k] != dp[i - 1][k]:
            total_money += requests[i - 1][1]
            accepted_requests += 1
            table_assignments.append((i, k))
            k -= 1

    print(accepted_requests)
    print(total_money)

    for request, table in zip(reversed(table_assignments), reversed([*range(k, 0, -1)])):
        print(f"{request} {table}")

