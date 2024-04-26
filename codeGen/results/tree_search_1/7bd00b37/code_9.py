MOD = 998244353

# Function to calculate factorial modulo MOD
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i % MOD
    return res

# Function to calculate modular inverse using Fermat's Little Theorem
def modinv(n):
    return pow(n, MOD - 2, MOD)

# Function to perform DFS and calculate the number of permutations for each subtree
def dfs(u, p):
    dp[u] = 1
    fact = 1
    for v in tree[u]:
        if v == p:
            continue
        dfs(v, u)
        dp[u] = dp[u] * dp[v] % MOD
        dp[u] = dp[u] * fact % MOD
        fact = fact * (size[v] + 1) % MOD
        size[u] += size[v] + 1

# Reading input
n = int(input())
tree = [[] for _ in range(n + 1)]
size = [0] * (n + 1)
dp = [0] * (n + 1)

# Building the tree
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Performing the DFS from node 1 (chosen arbitrarily as the root)
dfs(1, -1)

# Calculating the result for the entire tree
result = dp[1] * factorial(n - 1) % MOD
print(result)
