# Step 1: Read input
n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

# Step 2: Initialize variables
dp = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)
visited = set()

# Step 3: Build a graph using Dijkstra's algorithm to find shortest distances from vertex 1
pq = [(0, 1)]  # priority queue contains tuples of (distance, vertex)
while pq:
    d, u = heapq.heappop(pq)
    if d > dp[u]:
        continue
    for v, t in [(x[1], x[2]) for x in edges if x[0] == u]:
        new_d = d + t
        if new_d < dp[v]:
            dp[v] = new_d
            parent[v] = u
            heapq.heappush(pq, (new_d, v))

# Step 4: Find the maximum number of vertices that can be visited within T time units
k = 0
curr_time = T
while curr_time >= 0 and k < n:
    for i in range(n, -1, -1):
        if parent[i] != -1 and dp[i] <= curr_time:
            visited.add(i)
            curr_time -= dp[i]
            k += 1

# Step 5: Print the result
print(k)
print(*sorted(visited), sep=' ')
