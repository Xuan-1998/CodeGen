def dfs(graph, w, i, j):
    if dp[i][j] != -1:  # memoization
        return dp[i][j]
    
    result = -1
    for neighbor in graph[i]:
        if j + w[neighbor] <= w[i]:  # can still buy gas
            result = max(result, dfs(graph, w, neighbor, j + w[neighbor]))
    
    dp[i][j] = result
    return result

def solve():
    n = int(input())
    w = [0] * (n+1)  # maximum amount of gasoline at each city
    graph = [[] for _ in range(n+1)]  # road connectivity graph
    
    for i in range(1, n+1):
        w[i] = int(input())  # input the maximum amount of gas at each city
        
    for i in range(1, n+1):
        for j in range(i+1, n+1):  # connect two cities
            graph[i].append(j)
            graph[j].append(i)  # undirected graph
    
    dp = [[-1] * (1000010) for _ in range(n+1)]  # memoization array
    
    result = -1
    for i in range(1, n+1):
        result = max(result, dfs(graph, w, i, w[i]))
    
    print(result)

solve()
