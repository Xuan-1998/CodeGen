# Fill in the dp array
for i in range(2, n):
    for j in range(i+1, n+1):
        if any(t <= T for t in graph[i].values()):
            dp[i][j] = max(dp[i][j], dp[i-1][i-1] + 1)
        else:
            dp[i][j] = dp[i-1][i-1]

# Find the maximum number of vertices that can be visited
max_vertices = dp[0][n]

# Construct the actual route
i, j = n, max_vertices - 1
while i > 0:
    if i == j:
        result.append(i)
        break
    for vertex in range(n-1, -1, -1):
        if (vertex not in graph or any(t <= T for t in graph[vertex].values())) and dp[i][j] == dp[i-1][j]:
            result.append(vertex)
            i -= 1

# Print the maximum number of vertices that can be visited
print(max_vertices)

# Print the actual route
print(*result, sep='\n')
