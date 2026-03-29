import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def dfs(u, parent, dp, adj, k):
    dp[u][0] = 1
    count = 0

    for v in adj[u]:
        if v == parent:
            continue
        count += dfs(v, u, dp, adj, k)
        for d in range(1, k + 1):
            count += dp[u][d - 1] * dp[v][k - d]

        for d in range(1, k + 1):
            dp[u][d] += dp[v][d - 1]

    return count

def solve():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    adj = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = dfs(1, -1, dp, adj, k)
    
    print(result)

if __name__ == "__main__":
    solve()

