import sys

def dfs(node, mi, mx):
    if dp[node][k-1][mi, mx]:
        return (node, min(mi + val, mx + val), max(mi + val, mx + val))
    for neighbor in adj[node]:
        new_mi = min(mi, val)
        new_mx = max(mx, val)
        for i in range(2):
            if dp[neighbor][k-1-(i==0)][new_mi, new_mx]:
                return (node, new_mi, new_mx)
    return None

def solve():
    global k
    n, k = map(int, input().split())
    val = [int(x) for x in input().split()]
    adj = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    dp = [[[False]*11 for _ in range(10)] for _ in range(10)]
    for node in range(n):
        if len(adj[node]) > 0:
            mi, mx = dfs(node, float('-inf'), float('inf'))
            if mi == mx and k-1 >= 0:
                return "YES"
    
    return "NO"

while True:
    try:
        print(solve())
    except:
        break
