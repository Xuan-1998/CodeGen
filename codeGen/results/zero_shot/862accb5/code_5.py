def dfs(graph, node, parent, depth, depths, parents):
    depths[node] = depth
    parents[node] = parent
    for neighbor, length in graph[node]:
        if neighbor == parent:
            continue
        if depths[neighbor] == -1:
            # If the neighbor hasn't been visited, continue DFS
            dfs(graph, neighbor, node, depth + 1, depths, parents)
        else:
            # If the neighbor has been visited, we found a cycle
            if depths[node] > depths[neighbor]:
                # Return the edge that forms a cycle with the maximum depth difference
                return (node, neighbor, length)
    return None

def find_longest_road_in_cycle(graph, n):
    depths = [-1] * n
    parents = [-1] * n
    longest_road = (0, 0, 0)  # store the longest road as (node1, node2, length)

    for i in range(n):
        if depths[i] == -1:  # if the node hasn't been visited
            result = dfs(graph, i, -1, 0, depths, parents)
            if result:
                _, _, length = result
                if length > longest_road[2]:
                    longest_road = result

    return longest_road

def main():
    n = int(input().strip())
    graph = [[] for _ in range(n)]
    total_inconvenience = 0

    for _ in range(n):
        u, v, l = map(int, input().split())
        graph[u-1].append((v-1, l))
        graph[v-1].append((u-1, l))
        total_inconvenience += l

    _, _, longest_road_length = find_longest_road_in_cycle(graph, n)
    min_inconvenience = total_inconvenience - longest_road_length
    print(min_inconvenience)

if __name__ == "__main__":
    main()
