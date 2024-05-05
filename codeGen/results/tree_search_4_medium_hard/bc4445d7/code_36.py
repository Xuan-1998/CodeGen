import sys

def solve():
    n = int(input())
    tree_edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree_edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    memo = {}
    
    def dfs(node):
        if node == n:
            return 0
        
        if node not in memo:
            memo[node] = 0
            for child in children[node]:
                for label in range(1, k // (k % prime_factors[0])):
                    f = sum(tree_edges[i][2] for i in range(node) if tree_edges[i][1] == child)
                    dp[node + 1][k // (k % label)] = max(dp[node + 1][k // (k % label)], f + dfs(child))
                memo[node] = max(memo[node], dp[node + 1][k])
        
        return memo[node]
    
    children = {}
    for edge in tree_edges:
        if edge[0] not in children:
            children[edge[0]] = []
        children[edge[0]].append(edge[1])
    
    print((dfs(1) % (10**9 + 7)))

if __name__ == "__main__":
    solve()
