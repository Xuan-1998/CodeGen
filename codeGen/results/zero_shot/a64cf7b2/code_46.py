dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j, (v, t) in enumerate(graph[i]):
        if dp[v] + t <= T:
            dp[v] += t

k = max(dp[1:])
print(k)

# Print the indices of vertices that can be visited on the route from vertex 1 to vertex n
visited = []
t = k - 1
i = n
while i > 0 and t >= 0:
    for v, edge_t in graph[i]:
        if dp[v] + edge_t <= T and t >= edge_t:
            visited.append(i)
            t -= edge_t
            i = v
            break

print(*visited[::-1], sep='\n')
