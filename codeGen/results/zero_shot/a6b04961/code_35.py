    def calculate_beauty(connected_components):
        total_beauty = 0
        for component in connected_components:
            # Find the longest tail for this CC
            tail_length = max(len(path) for path in dfs_longest_path(component))
            
            # Count the number of spines
            spine_count = sum(len(spines) for _component, path, spines in dfs_spines(_component, component))
            
            total_beauty += tail_length * spine_count
        
        return total_beauty
    
    def dfs_longest_path(graph, node, visited, path):
        visited.add(node)
        if len(path) > 0:
            yield from [(path, [node])]
        for neighbor in graph[node]:
            if neighbor not in visited:
                yield from (dfs_longest_path(neighbor))
    
    def dfs_spines(graph, component):
        for node in component:
            visited = set()
            for neighbor, color in graph[node]:
                if neighbor not in visited and neighbor not in component:
                    yield (component, path, [node])
    
    # Step 6
    print(calculate_beauty(connected_components))  # Output the maximum beauty of a hedgehog
