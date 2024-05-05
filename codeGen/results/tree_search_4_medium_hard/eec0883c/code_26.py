from collections import defaultdict

def gas_stations():
    n = int(input())
    w = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    memo = {}
    def dfs(city, remaining_gasoline):
        if (city, remaining_gasoline) in memo:
            return memo[(city, remaining_gasoline)]
        
        if city == n-1:
            return remaining_gasoline
        
        max_flow = 0
        for neighbor, capacity in graph[city]:
            flow = min(capacity, w[neighbor] - remaining_gasoline)
            max_flow = max(max_flow, flow + dfs(neighbor, remaining_gasoline + flow))
        
        memo[(city, remaining_gasoline)] = max_flow
        return max_flow
    
    print(dfs(0, 0))

gas_stations()
