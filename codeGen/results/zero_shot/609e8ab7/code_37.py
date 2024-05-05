n = int(input())
p = list(map(int, input().split()))
ranges = []
for i in range(n):
    l, r = map(int, input().split())
    ranges.append((l, r))

def dfs(vertex, depth=0):
    depths[vertex] = depth
    if parent[vertex]:
        dfs(parent[vertex], depth + 1)
depths = {}
parent_vertex = n - 1
for i in range(n - 1, 0, -1):
    dfs(i, 0)

min_ops = 0
for i in range(n):
    l, r = ranges[i]
    for j in range(i, -1, -1):
        if depths[j] + 1 > min(ranges[j][1], r) - l:
            min_ops += 1
            break

print(min_ops)
