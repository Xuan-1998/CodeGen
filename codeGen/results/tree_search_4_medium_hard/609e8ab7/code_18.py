from collections import deque

def dfs(node, parent=None):
    dp[node] = max(dp[node], r[node] - l[node])
    
    for child in children[node]:
        if child != parent:
            dp[node] += dfs(child, node)
    
    return dp[node]

n = int(input())
dp = [0] * (n + 1)

for _ in range(n - 1):
    p = list(map(int, input().split()))
    for i, v in enumerate(p):
        children[v].append(i + 2)
        
r, l = zip(*[list(map(int, input().split())) for _ in range(n)])

res = [0]
dq = deque([1])
while dq:
    node = dq.popleft()
    res.append(dfs(node))
    
for x in res:
    print(x)
