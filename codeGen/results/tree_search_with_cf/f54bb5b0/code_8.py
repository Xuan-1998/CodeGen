python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs_with_distance_k(n, k, edges):
    # Build the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0] * (k + 1)
    
    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
        
        # Count pairs with exact distance k involving this node
        if k > 0:
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                for d in range(1, k):
                    result[k] += dp[neighbor][d - 1] * (dp[node][k - d] - dp[neighbor][k - d - 1])
        
    dfs(1, -1)
    return sum(result) // 2

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    print(count_pairs_with_distance_k(n, k, edges))

if __name__ == "__main__":
    main()

