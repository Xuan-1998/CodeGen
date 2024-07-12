python
import sys
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]
    
    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for i in range(k):
                result[0] += dp[node][i] * dp[neighbor][k - i - 1]
            for i in range(k):
                dp[node][i + 1] += dp[neighbor][i]
    
    dfs(1, -1)
    return result[0]

def main():
    input_data = input().strip().split()
    n = int(input_data[0])
    k = int(input_data[1])
    edges = []
    for i in range(2, len(input_data), 2):
        a = int(input_data[i])
        b = int(input_data[i + 1])
        edges.append((a, b))
    
    result = count_pairs(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

