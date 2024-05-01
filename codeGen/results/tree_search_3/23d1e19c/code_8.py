from collections import defaultdict

def min_max_recomputations(graph, fixed_path):
    n = len(graph)
    dp = {i: [0, 0] for i in range(n)}
    
    # Initialize the dictionary with default values
    for v in fixed_path:
        dp[v][0] = 1
    
    # Iterate over all vertices
    for i in range(n):
        if i not in fixed_path:
            continue
        
        # For each vertex, iterate over its neighbors
        for j in graph[i]:
            if j == i + 1:  # This is the next vertex in the path
                dp[i][0] = min(dp[i][0], dp[j][0])
                dp[i][1] = max(dp[i][1], dp[j][1])
            else:
                # If the neighbor is not in the fixed path, 
                # we need to recompute the shortest path from i
                if j not in fixed_path:
                    dp[i][0] += 1
                    dp[i][1] = max(dp[i][1], dp[j][1])
                else:
                    # If the neighbor is in the fixed path, 
                    # we just need to update the minimum and maximum recomputations
                    dp[i][0] = min(dp[i][0], dp[j][0])
                    dp[i][1] = max(dp[i][1], dp[j][1])
    
    return [dp[fixed_path[-1]][0], dp[fixed_path[-1]][1]]

# Example usage:
graph = [[1, 2], [2, 3], [3, 4]]
fixed_path = [1, 3]
print(min_max_recomputations(graph, fixed_path))
