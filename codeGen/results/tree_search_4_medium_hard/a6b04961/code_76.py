from collections import defaultdict

def maximum_hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {}
    def dfs(tail_length, vertex_index, visited=None):
        if visited is None:
            visited = set()
        if (tail_length, vertex_index) in memo:
            return memo[(tail_length, vertex_index)]
        
        max_beauty = 0
        for neighbor in graph.get(vertex_index, []):
            if neighbor not in visited:
                new_tail_length = tail_length + 1
                beauty = dfs(new_tail_length, neighbor, visited | {neighbor})
                if beauty > max_beauty:
                    max_beauty = beauty
        
        memo[(tail_length, vertex_index)] = max_beauty
        return max_beauty

    max_beauty = 0
    for i in range(1, n + 1):
        max_beauty = max(max_beauty, dfs(0, i))

    print(max_beauty)

if __name__ == "__main__":
    maximum_hedgehog_beauty()
