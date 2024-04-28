from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
k = int(input())
path = list(map(int, input().split()))
min_rec, max_rec = 0, k
q = deque([(i, 0) for i in range(k)])
while q:
    x, rec = q.popleft()
    if x == path[-1]:
        break
    for y in graph[x]:
        if y not in path[:x+1]:
            min_rec = min(min_rec, rec+1)
            max_rec = max(max_rec, rec+1)
            q.append((y, rec+1))
print(min_rec, max_rec)
