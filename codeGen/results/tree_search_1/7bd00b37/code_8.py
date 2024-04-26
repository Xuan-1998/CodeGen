MOD = 998244353

def dfs(node, parent, graph, dp, fact, inv_fact):
    dp[node] = 1
    size = 1
    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node, graph, dp, fact, inv_fact)
        size += dp[child]
        dp[node] = dp[node] * dp[child] % MOD * inv_fact[dp[child]] % MOD
    dp[node] = dp[node] * fact[size - 1] % MOD

def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    # Precompute factorials and their modular inverses
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Read the tree edges
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform DFS and dynamic programming
    dfs(1, 0, graph, dp, fact, inv_fact)
    
    # Output the result for the root
    print(dp[1])

if __name__ == "__main__":
    main()
