python
import sys
input = sys.stdin.read
sys.setrecursionlimit(100000)

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(n)
        return
    
    edges = []
    idx = 2
    for _ in range(n - 1):
        ai = int(data[idx]) - 1
        bi = int(data[idx + 1]) - 1
        edges.append((ai, bi))
        idx += 2
    
    adj = [[] for _ in range(n)]
    for ai, bi in edges:
        adj[ai].append(bi)
        adj[bi].append(ai)
    
    dp = [[0] * (k + 1) for _ in range(n)]
    result = [0]

    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for i in range(k):
                result[0] += dp[node][i] * dp[neighbor][k - i - 1]
            for i in range(1, k + 1):
                dp[node][i] += dp[neighbor][i - 1]

    dfs(0, -1)
    print(result[0])

solve()

