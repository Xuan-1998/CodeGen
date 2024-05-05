max_beauty = 0
for start in range(n):
    # Try to construct a simple path starting at vertex start
    path_len = 1
    current_vertex = start
    while True:
        # Find the next vertex on the path
        for neighbor in graph[current_vertex]:
            if neighbor not in path:
                path.append(neighbor)
                path_len += 1
                current_vertex = neighbor
                break
        else:
            # No more vertices to add, so stop here
            break

    # Count the number of spines for this tail
    spine_count = 0
    for edge in graph:
        if edge[0] not in path and edge[1] in path:
            spine_count += 1
        elif edge[0] in path and edge[1] not in path:
            spine_count += 1

    # Update the maximum beauty if necessary
    max_beauty = max(max_beauty, path_len * spine_count)

print(max_beauty)
