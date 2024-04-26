MOD = 998244353

def dfs(node, parent, graph, subtree_sizes, dp, factorial, inv_factorial):
    subtree_sizes[node] = 1
    dp[node][1] = 1

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node, graph, subtree_sizes, dp, factorial, inv_factorial)
        subtree_sizes[node] += subtree_sizes[child]

        # Combine child's ways with the current node's ways
        new_dp = [0] * (subtree_sizes[node] + 1)
        for i in range(1, subtree_sizes[node] - subtree_sizes[child] + 1):
            for j in range(1, subtree_sizes[child] + 1):
                new_dp[i + j] += dp[node][i] * dp[child][j] * factorial[i + j - 1] * inv_factorial[i - 1] * inv_factorial[j] % MOD
                new_dp[i + j] %= MOD
        dp[node] = new_dp

    # If node is not a leaf, multiply by the number of ways to insert the children permutations into the circle
    if subtree_sizes[node] > 1:
        dp[node][subtree_sizes[node]] = dp[node][subtree_sizes[node]] * inv_factorial[subtree_sizes[node] - 1] % MOD

def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Precompute factorials and inverse factorials for n
    factorial = [1] * (n + 1)
    inv_factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    inv_factorial[n] = pow(factorial[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

    # Initialize DP table and subtree sizes
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    subtree_sizes = [0] * (n + 1)

    # Start DFS from node 1
    dfs(1, -1, graph, subtree_sizes, dp, factorial, inv_factorial)

    # The answer is the number of ways to arrange the entire tree
    print(dp[1][n])

if __name__ == "__main__":
    main()
