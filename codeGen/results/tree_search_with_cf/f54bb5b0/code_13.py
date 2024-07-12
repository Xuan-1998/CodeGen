python
import sys
from collections import defaultdict, deque

input = sys.stdin.read
def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(0)
        return
    
    edges = []
    idx = 2
    for _ in range(n - 1):
        a = int(data[idx])
        b = int(data[idx + 1])
        edges.append((a, b))
        idx += 2
    
    # Building the tree using adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: path of length 0 from u to u
    for u in range(1, n + 1):
        dp[u][0] = 1
    
    # Function to perform DFS and fill dp table
    def dfs(node, parent):
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    # Start DFS from node 1 (or any arbitrary node, since it's a tree)
    dfs(1, -1)
    
    # Count the number of valid pairs
    result = 0
    for u in range(1, n + 1):
        result += dp[u][k]
    
    # Since each path is counted twice, divide the result by 2
    print(result // 2)

if __name__ == "__main__":
    main()

