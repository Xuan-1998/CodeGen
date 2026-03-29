from collections import defaultdict

n = int(input())
parent = [0] + list(map(int, input().split()))
range_values = []
for _ in range(n):
    l, r = map(int, input().split())
    range_values.append((l, r))

def dfs(i, j):
    if not children[i]:
        return j
    res = float('inf')
    for child in children[i]:
        res = min(res, 1 + dfs(child, max(0, min(j, range_values[child][1] - range_values[child][0]))))
    return res

children = defaultdict(list)
for i in range(2, n+1):
    parent[i-1]
    children[parent[i]].append(i)

dp = [[float('inf')] * (10**9 + 1) for _ in range(n+1)]
dp[1][range_values[1][1] - range_values[1][0]] = range_values[1][1] - range_values[1][0]

for i in range(2, n+1):
    for j in range(range_values[i][1] - range_values[i][0] + 1):
        dp[i][j] = min(dp[i][j], 1 + dfs(i, max(0, min(j, range_values[i][1] - range_values[i][0]))))

print(sum([min(dp[i][range_values[i][1] - range_values[i][0]] + 1) for i in range(2, n+1)]))
