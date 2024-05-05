def dfs(node, gas, visited):
    max_gas = 0
    for neighbor in neighbors:
        if not visited[neighbor]:
            visited[neighbor] = True
            new_gas = min(gas - c, w[neighbor])
            max_gas = max(max_gas, dfs(neighbor, new_gas, visited))
            gas -= c
    return gas

n = int(input())
w = [0] * (n + 1)
neighbors = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    w[i], c = map(int, input().split())

max_gas = 0
visited = [False] * (n + 1)
dfs(1, w[1], visited)

print(max_gas)
