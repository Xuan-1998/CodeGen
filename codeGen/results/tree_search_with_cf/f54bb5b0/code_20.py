python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(0)
        return
    
    edges = []
    for i in range(2, len(data), 2):
        a = int(data[i])
        b = int(data[i+1])
        edges.append((a, b))
    
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = 0
    
    def dfs(u, parent):
        nonlocal result
        dp[u][0] = 1
        
        for v in tree[u]:
            if v == parent:
                continue
            dfs(v, u)
            for d in range(1, k + 1):
                result += dp[u][d - 1] * dp[v][k - d]
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]
    
    dfs(1, -1)
    print(result)

if __name__ == "__main__":
    solve()

