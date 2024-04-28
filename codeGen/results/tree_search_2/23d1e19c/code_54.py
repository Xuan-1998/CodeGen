import heapq

n, m = map(int, input().split())
dp = [[float('inf'), 0] for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t, k = map(int, input().split())
path = list(map(int, input().split()))

pq = [(0, 0, s)]  # (dist, recomputation_times, vertex)
dp[s][0] = 0

while pq:
    dist, rec_time, cur_vertex = heapq.heappop(pq)

    if dp[cur_vertex][rec_time] < dist: continue
    for next_vertex in graph[cur_vertex]:
        if rec_time + 1 > k:
            break
        new_dist = dist + 1
        if new_dist < dp[next_vertex][rec_time+1]:
            dp[next_vertex][rec_time+1] = new_dist
            heapq.heappush(pq, (new_dist, rec_time+1, next_vertex))

min_max_recomputation_times = [max(dp[i][j] for i in range(n)) for j in range(k)]
print(min(min_max_recomputation_times), max(min_max_recomputation_times))
