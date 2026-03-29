def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    prime_factors = list(map(int, input().split()))

    dp = [[0] * (n-1) for _ in range(n)]
    mp = [[0] * (n-1) for _ in range(n)]

    # Populate the DP table
    for edge in edges:
        u, v = edge
        product = 1
        ones = 0
        for i in range(2, m+1):
            if prime_factors[i-1] not in (u, v):
                product *= prime_factors[i-1]
                ones += 1

        dp[u][v] = product
        mp[u][v] = ones
        # Update the DP table for other nodes as well
        for i in range(n-1):
            if edges[i][0] == u:
                edges[i][0] = v
            elif edges[i][1] == u:
                edges[i][1] = v

    max_distribution_index = 0
    # Iterate over all edges and update the maximum distribution index
    for edge in edges:
        u, v = edge
        product = dp[u][v]
        ones = mp[u][v]
        max_distribution_index += (product * ones) % (10**9 + 7)

    print(max_distribution_index)
