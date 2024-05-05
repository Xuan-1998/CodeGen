import sys

def dfs(graph, node, xor_value):
    visited = set()
    current_xor = xor_value
    while True:
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                current_xor ^= graph[neighbor]
                node = neighbor
                break
        else:
            return current_xor

def solve_case(n, k, values, edges):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    xor_values = set()
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        current_xor = values[start_node]
        while True:
            graph[start_node].remove(end_node)
            end_node = min((neighbor for neighbor in graph[end_node] if neighbor not in visited), key=lambda x: values[x])
            current_xor ^= values[end_node]
            start_node = end_node
            visited.add(start_node)
            if len(graph[start_node]) == 0:
                break
        xor_values.add(current_xor)

    xor_values = sorted(list(xor_values))
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        current_xor = values[start_node]
        while True:
            graph[start_node].remove(end_node)
            end_node = min((neighbor for neighbor in graph[end_node] if neighbor not in visited), key=lambda x: values[x])
            current_xor ^= values[end_node]
            start_node = end_node
            visited.add(start_node)
            if len(graph[start_node]) == 0:
                break
        if current_xor not in xor_values[:k-1]:
            return "NO"
    return "YES"

def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        print(solve_case(n, k, values, edges))

if __name__ == "__main__":
    main()
