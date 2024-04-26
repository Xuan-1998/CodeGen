MOD = 998244353

def mul(a, b):
    return (a * b) % MOD

def add(a, b):
    return (a + b) % MOD

def mod_inv(a):
    return pow(a, MOD - 2, MOD)

def dfs(node, parent):
    dp[node] = 1
    subtree_size = 1
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node] = mul(dp[node], dp[child])
            dp[node] = mul(dp[node], mod_inv(fact[subtree_size]))
            dp[node] = mul(dp[node], fact[subtree_size + sizes[child] - 1])
            subtree_size += sizes[child]
    sizes[node] = subtree_size

n = int(input())
tree = [[] for _ in range(n + 1)]
sizes = [0] * (n + 1)
dp = [0] * (n + 1)
fact = [1] * (n + 1)

# Precompute factorials and modular inverses
for i in range(2, n + 1):
    fact[i] = mul(fact[i - 1], i)

# Read tree edges
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Perform DFS and DP
dfs(1, -1)

# The answer is the number of valid permutations for the root
print(dp[1])
