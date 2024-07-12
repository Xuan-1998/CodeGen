python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(n * (n - 1) // 2)
        return
    
    edges = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n - 1)]
    
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
    print(result[0])

if __name__ == "__main__":
    solve()

