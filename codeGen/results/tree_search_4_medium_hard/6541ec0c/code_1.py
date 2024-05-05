import sys
from collections import defaultdict

def dfs(node, parent):
    if node not in children:
        return 0
    
    total_xor = children[node]
    for child in children[node]:
        if child != parent:
            total_xor ^= dfs(child, node)
    
    dp[node][1] = (total_xor == 0) or (parent >= k and dp[parent][k-1])
    for i in range(2, min(k+1, len(children)+1)):
        dp[node][i] = dp[node][i-1] and all(dp[child][max(i-1, 0)] for child in children[node] if child != parent)
    
    return total_xor

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    children = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        children[u].append(v)
        children[v].append(u)
    
    dp = [[False] * (k+1) for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, n+1):
        total_xor = values[i-1]
        for j in range(min(k+1, len(children)+1)):
            if j == 0:
                dp[i][j] = (total_xor == 0)
            elif j == 1:
                dp[i][j] = True
            else:
                parent = children.get(i)
                if parent:
                    total_xor ^= dfs(parent, i)
                    dp[i][j] = dp[i][j-1] and all(dp[child][max(j-1, 0)] for child in children[i] if child != parent)
    
    return "YES" if dp[0][k] else "NO"

print(solve())
