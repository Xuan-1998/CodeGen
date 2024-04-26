MOD = 998244353

def dfs(u, parent):
    dp[u][1] = 1  # Base case for leaf node
    size_u = 1
    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)
        size_v = sum(dp[v])
        new_dp_u = [0] * (size_u + size_v + 1)
        # Merge permutations of subtrees of children
        for i in range(1, size_u + 1):
            for j in range(1, size_v + 1):
                new_dp_u[i + j] += dp[u][i] * dp[v][j]
                new_dp_u[i + j] %= MOD
        dp[u] = new_dp_u
        size_u += size_v
    # Multiply by the number of ways to insert the subtrees around u
    for i in range(1, size_u + 1):
        dp[u][i] *= factorial[i - 1]
        dp[u][i] %= MOD

# Input handling
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Initialize DP table and factorial array
dp = [[0] * (n + 1) for _ in range(n + 1)]
factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

# Run DFS and DP
dfs(1, -1)

# Output the result
print(dp[1][n])
