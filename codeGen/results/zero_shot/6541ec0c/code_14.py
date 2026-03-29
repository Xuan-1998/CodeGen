from collections import defaultdict
import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n+1)
    dfs_values = []
    
    def dfs(node, parent):
        nonlocal dfs_values
        visited[node] = True
        bit_value = 0
        for neighbor in graph[node]:
            if neighbor != parent:
                if not visited[neighbor]:
                    dfs(neighbor, node)
                    bit_value ^= dfs_values[-1]
                else:
                    bit_value ^= values[neighbor-1]
                dfs_values.append(bit_value)
    
    dfs(1, -1)
    
    res = "YES"
    for bit in dfs_values[:-k+1]:
        if len(set(bin(val)[2:] for val in dfs_values[k-1:])) > 1:
            res = "NO"
            break
    
    print(res)

if __name__ == "__main__":
    solve()
