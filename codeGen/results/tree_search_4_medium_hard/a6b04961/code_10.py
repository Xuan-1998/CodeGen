import sys

def dp(graph):
    memo = {}
    def dfs(tail, last_vertex):
        if (tail, last_vertex) in memo:
            return memo[(tail, last_vertex)]
        
        max_beauty = 1
        for edge in graph[last_vertex]:
            if edge not in tail:
                new_tail = list(tail)
                new_tail.append(edge)
                beauty = dfs(new_tail, edge)[0] + (len(tail) + 1)
                max_beauty = max(max_beauty, beauty)
        
        memo[(tail, last_vertex)] = (max_beauty, len(tail))
        return (max_beauty, len(tail))

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    max_beauty = 0
    for i in range(n):
        beauty, _ = dfs([i], i)
        max_beauty = max(max_beauty, beauty)

    print(max_beauty)
