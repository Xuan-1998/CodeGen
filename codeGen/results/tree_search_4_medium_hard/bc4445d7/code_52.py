def calculate_distribution_index(n, edges, k):
    memo = [[[0]*1000001 for _ in range(6*10000)] for _ in range(10**5+1)]
    
    def dfs(i, j, k):
        if i > n: return 0
        if k == 1: return 0
        if memo[i][j][k] != 0: return memo[i][j][k]
        
        left = dfs(edges[0], edges[1])
        right = dfs(edges[2], edges[3])
        sum_edge = sum(f(i, j) for j in range(i+1, n))
        dp[i][j][k] = max(left, right) + sum_edge
        
        return dp[i][j][k]
    
    max_distribution_index = 0
    for i in range(2, n):
        dfs(i, edges[0], k)
    
    print(max_distribution_index % (10**9 + 7))

# Example usage:
n = int(input())
edges = []
m = int(input())
prime_factors = list(map(int, input().split()))
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))
calculate_distribution_index(n, edges, reduce(operator.mul, prime_factors, 1))
