import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # This will store the number of valid pairs
    result = 0

    def dfs(node, parent):
        # dp[i] will store the number of nodes at distance i from the current node
        dp = [0] * (k + 1)
        dp[0] = 1  # The distance from the node to itself is 0

        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp = dfs(neighbor, node)
            # For each pair of distances from node and child, check if they sum to k
            for i in range(k):
                for j in range(k - i):
                    result += dp[i] * child_dp[j]
            # Merge child_dp into dp
            for i in range(k):
                dp[i + 1] += child_dp[i]

        return dp

    # Start DFS from node 1 (assuming nodes are 1-indexed)
    dfs(1, -1)

    return result

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    for i in range(2, len(data), 2):
        a = int(data[i])
        b = int(data[i + 1])
        edges.append((a, b))
    
    print(count_pairs(n, k, edges))

