def dfs(city, total_gasoline):
    for neighbor, length in graph[city].items():
        new_total = min(total_gasoline - length, w[neighbor])
        if new_total > 0:
            result = max(result, new_total)
            dfs(neighbor, new_total)

result = 0
dfs(1, w[0])  # Start from city 1 with initial gasoline

print(result)  # Print the maximum amount of gasoline that Nut can have at the end
