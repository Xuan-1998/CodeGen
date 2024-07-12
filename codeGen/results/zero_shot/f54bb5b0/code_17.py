python
import sys
from collections import defaultdict, deque

def count_pairs_with_path_length_k(n, k, edges):
    # Create adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # DP array to store the count of paths of different lengths ending at each node
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]

    def dfs(node, parent):
        dp[node][0] = 1  # There is one path of length 0 ending at each node (the node itself)
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for i in range(1, k + 1):
                result[0] += dp[node][i - 1] * dp[neighbor][k - i]
            for i in range(1, k + 1):
                dp[node][i] += dp[neighbor][i - 1]

    dfs(1, -1)
    return result[0]

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

    result = count_pairs_with_path_length_k(n, k, edges)
    print(result)

