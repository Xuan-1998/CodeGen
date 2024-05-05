import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    parent = {}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if u not in parent:
            parent[u] = []
        if v not in parent:
            parent[v] = []
        parent[v].append(u)
    
    dp = [[[] for _ in range(2 ** k + 1)] for _ in range(max(values) + 1)]
    
    for node_val, edges in parent.items():
        prev_node_val = None
        for edge_count, (u, v) in enumerate(edges):
            if u == node_val:
                prev_node_val = v
            else:
                prev_node_val = u
            
            dp[node_val][edge_count + 1] = [x and (prev_node_val ^ node_val == 0) for x in dp[prev_node_val][edge_count]]
    
    ans = "NO"
    for node_val, edges in parent.items():
        if all(any(x and y for x, y in zip(dp[node_val][i], dp[node_val][j])) 
              for i in range(len(edges)) for j in range(i + 1, len(edges))):
            ans = "YES"
            break
    
    print(ans)

if __name__ == "__main__":
    solve()
