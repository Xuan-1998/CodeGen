===BEGIN CODE===
from collections import defaultdict

def hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {0: 1}

    def dfs(tail, last_vertex):
        if tail not in memo:
            memo[tail] = 0
            for neighbor in graph[last_vertex]:
                if neighbor not in tail:
                    memo[tail] = max(memo[tail], dfs(tail | {neighbor}, neighbor) + len(tail))
        return memo[tail]

    beauty = 0
    for i in range(1, n+1):
        beauty = max(beauty, dfs({i}, i))

    print(beauty)
===END CODE===
