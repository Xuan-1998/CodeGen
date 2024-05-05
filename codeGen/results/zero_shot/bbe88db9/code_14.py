n = int(input())
portal_list = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i].append(portal_list[i - 1])
    if i > 1:
        graph[portal_list[i - 2]].append(i)
visited = [False] * (n + 1)
path_length = 0

def dfs(room):
    global path_length
    visited[room] = True
    if room == n + 1:
        return path_length
    for neighbor in graph[room]:
        if not visited[neighbor]:
            path_length += 1
            result = dfs(neighbor)
            if result != -1:
                return result
    return -1

result = dfs(1)
print(result % (10**9 + 7))
