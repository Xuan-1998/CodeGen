import sys

def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    max_beauty = 0
    for last_node_in_tail in range(1, n + 1):
        for nodes_in_tail in range(last_node_in_tail):
            if dp[nodes_in_tail - 1][last_node_in_tail]:
                beauty = (last_node_in_tail - nodes_in_tail) * (n - last_node_in_tail)
                max_beauty = max(max_beauty, beauty + dp[nodes_in_tail - 1][last_node_in_tail])
            for next_node in graph.get(last_node_in_tail, []):
                if next_node not in range(nodes_in_tail, last_node_in_tail):
                    dp[next_node][last_node_in_tail] = max(dp[next_node][last_node_in_tail], beauty + 1)

    print(max_beauty)


if __name__ == "__main__":
    solve()
