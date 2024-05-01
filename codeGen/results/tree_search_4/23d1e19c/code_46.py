from collections import defaultdict

def recomputation_needed(n, m, edges, k, path):
    # Initialize dp and memo with base case at vertex t
    dp = [[(float('inf'), 0) for _ in range(n)] for _ in range(n)]
    memo = {(i, n-1): (0, 0) for i in range(n)}
    
    for u, v in edges:
        # Calculate f(v) using memoization
        if (v, n-1) not in memo:
            min_recom, max_recom = float('inf'), 0
            for j in range(k-1):
                w = path[j]
                min_recom = min(min_recom, dp[w][v][0])
                max_recom = max(max_recom, dp[w][v][1])
            memo[(v, n-1)] = (min_recom, max_recom)
        
        # Update dp[u][v] with f(v) and previous values
        min_recom, max_recom = memo[(v, n-1)]
        for j in range(k-1):
            w = path[j]
            min_dp, max_dp = dp[w][v]
            dp[u][v] = (min(min_dp, min_recom), max(max_dp, max_recom))
    
    # Return the minimum and maximum number of recomputations needed from s to t
    return dp[s][n-1]

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

print(recomputation_needed(n, m, edges, k, path))
