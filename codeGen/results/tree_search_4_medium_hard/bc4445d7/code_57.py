def solve(n, edges, m, prime_factors):
    # Initialize memoization table
    memo = [[0] * (n + 1) for _ in range(n + 1)]

    def dfs(u, v):
        # Base case: leaf node or only one child
        if u == n - 1:
            return 1

        # Memoized state transition function
        if memo[u][v]:
            return memo[u][v]

        # Compute product of edge labels on shortest path from u to root
        product = 1
        for i in range(v + 1, n):
            product *= edges[i - 1]
        product /= prime_factors[m - 1]

        # Update maximum possible distribution index for node u
        dp_u = 0
        for i in range(1, v):
            dp_u += dfs(i, u)
        dp_u += (product * (v + 1))

        # Memoize state transition function result
        memo[u][v] = dp_u

        return dp_u

    # Compute maximum possible distribution index for all nodes
    max_distribution_index = 0
    for i in range(1, n):
        max_distribution_index += dfs(i, 0)

    print(max_distribution_index % (10**9 + 7))

# Read input from stdin
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
m = int(input())
prime_factors = list(map(int, input().split()))

solve(n, edges, m, prime_factors)
