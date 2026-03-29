def find_max_distribution_index(n, edges, prime_factors):
    # Calculate all possible sums that can be achieved by labeling each edge with a positive integer such that the product of all n-1 numbers equals a given number k
    dp = [[float('inf')] * (n+1) for _ in range(2)]
    dp[0][1] = 0

    for u, v in edges:
        for i in range(n, -1, -1):
            if i >= v:
                dp[1][i] = min(dp[1][i], dp[0][v-1] + (u-v))
            else:
                dp[0][i] = min(dp[0][i], dp[1][v-1] + (v-i))

    max_distribution_index = 0
    for i in range(2, n+1):
        max_distribution_index += dp[1][i]

    return max_distribution_index % (10**9 + 7)

# Read input from standard input
T = int(input())
for _ in range(T):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p

    print(find_max_distribution_index(n, edges, prime_factors))
