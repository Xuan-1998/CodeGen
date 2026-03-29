def process_queries(signs, queries):
    n = len(signs)
    q = len(queries)

    # Initialize prefix sum array
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + (1 if signs[i] == "+" else -1)

    # Initialize dynamic programming arrays
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    ans = []
    for l, r in queries:
        # Calculate prefix sum for the query range
        ps_range = ps[r] - (ps[l - 1] if l > 0 else 0)

        # Update dynamic programming arrays for the query range
        for j in range(l - 1, r):
            if ps[j] >= 0:
                dp[ps_range][j] = min(dp[ps_range - 1][k] + (1 if signs[k] == "+" else -1) for k in range(l - 1, r))
            else:
                dp[ps_range][j] = dp[ps_range - 1][j]

        # The answer for the query is the minimum value in the range [l..r]
        ans.append(min(dp[ps_range][k] for k in range(l - 1, r)))

    return ans

# Receive inputs from stdin
n, q = map(int, input().split())
signs = list(input())
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

ans = process_queries(signs, queries)

# Print answers to stdout
print(*ans, sep='\n')
