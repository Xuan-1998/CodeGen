import sys

def find_cycle(parents, u, v):
    cycle = []
    while u != v:
        if u > v:
            cycle.append((u, parents[u]))
            u = parents[u]
        else:
            cycle.append((v, parents[v]))
            v = parents[v]
    cycle.append((u, v))
    return cycle

def dfs(graph, start, parents):
    stack = [(start, -1)]
    while stack:
        node, parent = stack.pop()
        for neighbor, length in graph[node]:
            if neighbor == parent:
                continue
            if parents[neighbor] == -1:
                parents[neighbor] = node
                stack.append((neighbor, node))
            else:
                return find_cycle(parents, node, neighbor)
    return None

def main():
    n = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n+1)]
    edge_lengths = {}
    total_length = 0
    
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, l))
        graph[v].append((u, l))
        edge_lengths[(u, v)] = l
        edge_lengths[(v, u)] = l
        total_length += l

    parents = [-1] * (n + 1)
    cycle = dfs(graph, 1, parents)

    min_inconvenience = float('inf')
    for u, v in cycle:
        inconvenience = total_length - edge_lengths[(u, v)]
        min_inconvenience = min(min_inconvenience, inconvenience)

    print(min_inconvenience)

if __name__ == "__main__":
    main()
