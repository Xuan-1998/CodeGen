code
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0] * (n+1) for _ in range(m+1)]

def solve(tail, last_node_in_tail, edges_left):
    if len(tail) == n:
        return 0
    if not edges_left:
        return 0

    beauty = 0
    for node in tail:
        for neighbor in graph[node]:
            if neighbor != last_node_in_tail and neighbor not in tail:
                new_tail = list(tail)
                new_tail.append(neighbor)
                beauty = max(beauty, solve(new_tail, neighbor, edges_left - 1))
    return (n - len(tail)) * len(tail) + beauty

print(solve([], 0, m))
