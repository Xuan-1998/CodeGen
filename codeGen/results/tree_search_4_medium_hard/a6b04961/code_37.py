from collections import defaultdict

def hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {}
    def dp(tail_length, edge_index):
        if (tail_length, edge_index) in memo:
            return memo[(tail_length, edge_index)]
        
        max_beauty = 0
        for next_edge in graph[edge_index]:
            if next_edge not in [u for u in range(n) if graph[u] and u <= tail_length]:
                new_tail_length = tail_length + 1
                beauty = dp(new_tail_length, next_edge)
                max_beauty = max(max_beauty, beauty)

        return memo[(tail_length, edge_index)] = max_beauty

    print(dp(0, 0))
