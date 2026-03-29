from collections import defaultdict

def hedgehog_beauty(n, m, edges):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    memo = [[0] * (n + 1) for _ in range(m + 1)]

    def dfs(tail_len):
        if tail_len > n:
            return 0
        if memo[tail_len][tail_len]:
            return memo[tail_len][tail_len]
        
        max_beauty = 0
        for u, neighbors in graph.items():
            if len(neighbors) == 1:
                # Edge can be added to the tail without extending its length
                beauty = (tail_len + 1) * (n - u)
                max_beauty = max(max_beauty, beauty)

        for i in range(tail_len):
            # Try adding edges from the current last vertex to all other vertices
            for v, neighbors in graph.items():
                if len(neighbors) > 0 and v not in graph[i]:
                    new_tail_len = i + 1
                    beauty = (new_tail_len - i) * (n - v)
                    max_beauty = max(max_beauty, beauty + dfs(new_tail_len))

        memo[tail_len][tail_len] = max_beauty
        return max_beauty

    max_beauty = 0
    for tail_len in range(1, n + 1):
        max_beauty = max(max_beauty, dfs(tail_len))
    return max_beauty

n, m = map(int, input().split())
edges = [(i, j) for i in range(m) for j in print().split()[1:]]

print(hedgehog_beauty(n, m, edges))
