MOD = 998244353

# Function to compute factorial modulo MOD
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = (fact * i) % MOD
    return fact

# Function to compute modular inverse
def modinv(a, p):
    return pow(a, p - 2, p)

# Function to compute nCr modulo MOD
def nCr(n, r):
    if r > n:
        return 0
    return (factorial(n) * modinv(factorial(r), MOD) * modinv(factorial(n - r), MOD)) % MOD

# DFS function to compute the number of permutations for each node
def dfs(u, parent):
    global dp, graph, subtree_size
    dp[u][0] = 1
    subtree_size[u] = 1
    for v in graph[u]:
        if v != parent:
            dfs(v, u)
            for i in range(subtree_size[u], -1, -1):
                for j in range(1, subtree_size[v] + 1):
                    dp[u][i + j] = (dp[u][i + j] + dp[u][i] * dp[v][j] * nCr(i + j, j)) % MOD
            subtree_size[u] += subtree_size[v]

# Read input
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Initialize DP table and subtree sizes
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
subtree_size = [0] * (n + 1)

# Run DFS to compute the answer
dfs(1, -1)

# The answer is the number of permutations for the root node
print(dp[1][n])
