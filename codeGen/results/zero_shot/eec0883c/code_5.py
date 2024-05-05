def dfs(node, parent, gas):
    for neighbor in roads:
        if neighbor[0] == node:  # neighbor is connected to node
            next_node = neighbor[1]
            next_gas = min(w[next_node], w[node] - neighbor[2])  # minimum gasoline at the next city
            if next_gas > 0 and not visited[next_node]:  # if there's still gas left and we haven't visited this city yet
                visited[next_node] = True
                dfs(next_node, node, next_gas)  # recursively traverse the tree

    return max(gas)  # return the maximum gasoline amount

visited = [False] * n
max_gas = 0
for i in range(n):
    if not visited[i]:  # visit each city for the first time
        gas = w[i]
        dfs(i, -1, gas)  # start DFS from this city
        max_gas = max(max_gas, gas)

print(max_gas)
