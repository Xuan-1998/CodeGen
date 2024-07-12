python
import sys
import collections

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Build the tree as an adjacency list
    tree = collections.defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize the DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]  # Use a list to allow modification within nested function

    def dfs(node, parent):
        dp[node][0] = 1  # Base case: distance 0 from itself
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            # Calculate pairs between node and its subtree rooted at neighbor
            for d in range(1, k + 1):
                result[0] += dp[neighbor][d - 1] * dp[node][k - d]
            # Update dp[node] using dp[neighbor]
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]

    # Start DFS from node 1 (assuming 1-based indexing)
    dfs(1, -1)
    return result[0]

if __name__ == "__main__":
    import sys
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
    
    print(count_pairs(n, k, edges))

