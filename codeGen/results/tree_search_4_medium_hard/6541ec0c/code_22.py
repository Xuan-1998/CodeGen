def solve(n, k, values):
    memo = {}
    
    def dfs(i, mi, mx):
        if (i, mi, mx) in memo:
            return memo[(i, mi, mx)]
        
        if i >= n:
            return "YES" if all(values[i-1] ^ val == 0 for j, val in enumerate(values)) else "NO"
        
        result = "YES"
        for child in [j for j in range(n) if parent[i][j]]:
            if (child, mi, mx) not in memo:
                memo[(child, mi, mx)] = dfs(child, mi ^ values[child], mx)
            result = min(result, memo[(child, mi, mx)])
        return "YES" if all(values[i-1] ^ val == 0 for j, val in enumerate(values)) else result
        
    parent = [[] for _ in range(n)]
    
    for u, v in zip(*[iter(map(int, input().split())) for _ in range(n-1)]):
        parent[u].append(v)
        parent[v].append(u)
        
    values = list(map(int, input().split()))
    
    return "YES" if dfs(0, 0, max(values)) == "YES" else "NO"
