from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))
    
    # Sort the edges by value
    edges.sort(key=lambda x: values[x[0]])
    
    dp = [[[float('inf')] * (k+1) for _ in range(k+1)] for _ in range(n)]
    
    memo = {}
    
    def dfs(node, min_xor, max_xor):
        if node >= n:
            return 0
        if (node, min_xor, max_xor) in memo:
            return memo[(node, min_xor, max_xor)]
        
        # Base case: If we are at the last node, there is no more edges to remove
        if node == n-1:
            return 0
        
        # Try removing each edge from the current node and recursively explore
        res = float('inf')
        for i in range(n):
            if (i, node) not in edges and values[i] ^ values[node] >= min_xor and values[i] ^ values[node] <= max_xor:
                res = min(res, 1 + dfs(i, values[i]^values[node], values[i]^values[node]))
        
        # Store the result for later use
        memo[(node, min_xor, max_xor)] = res
        
        return res
    
    print('YES' if dfs(0, 0, 0) <= k else 'NO')

if __name__ == "__main__":
    solve()
