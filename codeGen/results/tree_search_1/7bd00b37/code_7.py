from collections import defaultdict
from math import factorial
from sys import stdin, stdout

MOD = 998244353

def dfs(node, parent):
    size = 1
    dp[node] = 1
    for child in graph[node]:
        if child == parent:
            continue
        child_size = dfs(child, node)
        size += child_size
        dp[node] = dp[node] * dp[child] * inv_factorials[child_size] % MOD
    dp[node] = dp[node] * factorials[size - 1] % MOD
    return size

def mod_inv(x, mod):
    return pow(x, mod - 2, mod)

# Read input
n = int(stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Precompute factorials and their modular inverses
factorials = [1] * (n + 1)
inv_factorials = [1] * (n + 1)
for i in range(2, n + 1):
    factorials[i] = factorials[i - 1] * i % MOD
    inv_factorials[i] = mod_inv(factorials[i], MOD)

# Initialize DP array
dp = [0] * (n + 1)

# Perform DFS and DP
dfs(1, -1)

# Output the result for the root
stdout.write(str(dp[1]))
