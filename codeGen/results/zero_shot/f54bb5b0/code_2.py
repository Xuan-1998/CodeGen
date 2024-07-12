python
import sys
from collections import defaultdict

def dfs(node, parent, depth, count, adj):
    count[depth] += 1
    for neighbor in adj[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, count, adj)

def count_pairs_with_distance_k(n, k, edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    total_pairs = 0
    
    for node in range(1, n + 1):
        count = [0] * (k + 1)
        dfs(node, -1, 0, count, adj)
        
        for i in range(1, k // 2 + 1):
            total_pairs += count[i] * count[k - i]
        
        if k % 2 == 0:
            total_pairs += count[k // 2] * (count[k // 2] - 1) // 2
    
    return total_pairs

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    result = count_pairs_with_distance_k(n, k, edges)
    print(result)

