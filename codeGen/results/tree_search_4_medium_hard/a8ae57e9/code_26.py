def solve():
    n, k, max_capacity = [int(x) for x in input().split()]
    c = []
    for _ in range(n):
        group_size, total_spend = [int(x) for x in input().split()]
        c.append((group_size, total_spend))

    dp1 = {0: 0}
    dp2 = {0: k}

    for i in range(1, n+1):
        max_earn = 0
        min_tables = k
        for j in range(i):
            if c[j][0] <= max_capacity and dp1.get(j, 0) + c[i-1][1] > max_earn:
                max_earn = dp1.get(j, 0) + c[i-1][1]
                min_tables = min(min_tables, dp2.get(j, k))
        dp1[i] = max_earn
        dp2[i] = min_tables

    accepted_requests = []
    total_spend = 0
    for i in range(n, 0, -1):
        if c[i-1][1] == dp1[i]:
            accepted_requests.append((i, dp2[i]))
            total_spend += c[i-1][1]
            k -= 1

    print(f"{len(accepted_requests)} {total_spend}")
    for request, table in accepted_requests:
        print(f"{request} {table}")

solve()
