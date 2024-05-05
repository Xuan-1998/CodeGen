import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    graph = {}
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    dp = [[True] * (k+1) for _ in range(n+1)]

    def dfs(node, parent):
        xor_sum = values[node]
        for child in graph.get(node, []):
            if child != parent:
                xor_sum ^= values[child]
                dfs(child, node)
        return xor_sum

    for i in range(2, n+1):
        for j in range(k+1):
            dp[i][j] = all(xor == values[i] for xor in set(dfs(i, parent) for parent in graph.get(i, []) if parent is not None))

    print("YES" if dp[1][k-1] else "NO")

if __name__ == "__main__":
    solve()
