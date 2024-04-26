from collections import defaultdict
from math import factorial
from sys import stdin

MOD = 998244353

# Function to calculate n! % MOD
def mod_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = (f * i) % MOD
    return f

# Function to calculate (a^b) % MOD
def mod_pow(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result

# Function to calculate modular multiplicative inverse of a modulo MOD
def mod_inv(a):
    return mod_pow(a, MOD - 2)

# Function to calculate nCr % MOD
def mod_comb(n, r):
    if r > n:
        return 0
    return (mod_factorial(n) * mod_inv(mod_factorial(r)) % MOD * mod_inv(mod_factorial(n - r)) % MOD) % MOD

# DFS function to count permutations
def dfs(node, parent):
    global tree, dp, sizes
    dp[node] = 1
    size = 1
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node] = dp[node] * dp[child] % MOD * mod_comb(size + sizes[child] - 1, sizes[child]) % MOD
            size += sizes[child]
    sizes[node] = size

# Read input
n = int(stdin.readline().strip())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

# Initialize DP table and subtree sizes
dp = [0] * (n + 1)
sizes = [0] * (n + 1)

# Perform DFS and count permutations
dfs(1, -1)

# Output the result for the root
print(dp[1])
