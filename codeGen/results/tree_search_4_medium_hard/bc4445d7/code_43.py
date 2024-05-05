def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p

    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # initialize base case: each leaf node has one way to distribute ones
    for i in range(2, n+1):
        if len(edges[i-2][1:]) == 0:
            dp[i][0] = 1

    for u, v in edges:
        number_of_prime_factors_u_v = sum(p in prime_factors for p in set(v))
        dp[u][number_of_prime_factors_u_v] = max(dp[u][number_of_prime_factors_u_v], 1)
        
        for w in range(u+1, n+1):
            if len(edges[w-1][1:]) == 0:
                continue
            number_of_prime_factors_u_w = sum(p in prime_factors for p in set(w))
            dp[u][number_of_prime_factors_u_v] += dp[w][number_of_prime_factors_u_w]
        
    return dp[1][m] % (10**9 + 7)

print(solve())
