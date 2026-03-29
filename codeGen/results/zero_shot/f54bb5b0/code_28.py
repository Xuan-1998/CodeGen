import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(n * (n - 1) // 2)
        return
    
    adj = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        a = int(data[index]) - 1
        b = int(data[index + 1]) - 1
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
    dp = [[0] * (k + 1) for _ in range(n)]
    result = [0]
    
    def dfs(v, parent):
        dp[v][0] = 1
        for u in adj[v]:
            if u == parent:
                continue
            dfs(u, v)
            for d in range(1, k + 1):
                result[0] += dp[v][d - 1] * dp[u][k - d]
            for d in range(1, k + 1):
                dp[v][d] += dp[u][d - 1]
    
    dfs(0, -1)
    
    print(result[0])


