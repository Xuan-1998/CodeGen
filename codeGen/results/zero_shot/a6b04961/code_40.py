import sys

def find_longest_tail(graph):
    # Initialize variables
    longest_tail = []
    visited = [False] * len(graph)

    def dfs(v, path):
        visited[v] = True
        path.append(v)
        if not graph[v]:
            return 1
        max_length = 0
        for neighbor in range(len(graph)):
            if not visited[neighbor] and graph[v][neighbor]:
                length = dfs(neighbor, path[:])
                if length > max_length:
                    max_length = length
        return max_length + 1

    # Find the longest tail
    max_length = 0
    for i in range(len(graph)):
        if not visited[i]:
            length = dfs(i, [])
            if length > max_length:
                max_length = length
                longest_tail = []
                stack = [(i, [i])]
                while stack:
                    v, path = stack.pop()
                    if len(path) > max_length - 1:
                        break
                    for neighbor in range(len(graph)):
                        if not visited[neighbor] and graph[v][neighbor]:
                            stack.append((neighbor, path + [neighbor]))
                longest_tail = path

    return longest_tail

def count_spines(graph, tail):
    spines = 0
    for edge in range(len(graph)):
        u, v = graph[edge]
        if u in tail or v in tail:
            continue
        if (u in tail and v not in tail) or (v in tail and u not in tail):
            spines += 1
    return spines

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # Find the longest tail
    tail = find_longest_tail(graph)

    # Count spines
    spines = count_spines(graph, tail)

    # Calculate beauty
    beauty = len(tail) * spines

    print(beauty)

if __name__ == "__main__":
    main()
