python
import sys
input = sys.stdin.read
from collections import defaultdict

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if n == 1:
        print(0)
        return
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]
    
    def dfs(node, parent):
        dp[node][0] = 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            
            for i in range(1, k + 1):
                dp[node][i] += dp[neighbor][i - 1]
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            for i in range(1, k):
                result[0] += dp[neighbor][i - 1] * (dp[node][k - i] - dp[neighbor][k - i - 1])
        result[0] += dp[node][k]
    
    dfs(1, -1)
    print(result[0])

solve()

