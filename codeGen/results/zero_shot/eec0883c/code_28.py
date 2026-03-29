import heapq

n = int(input())
w = list(map(int, input().split()))
roads = [[] for _ in range(n)]
dp = [0] * n

for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads[u].append((v, c))
    roads[v].append((u, c))
    
    max_gas_u = w[u] - c
    max_gas_v = w[v] - c
    
    if max_gas_u > dp[u]:
        dp[u] = max_gas_u
    if max_gas_v > dp[v]:
        dp[v] = max_gas_v
        
    heapq.heappush(heap, (dp[u], u))

end_node = int(input())
while heap:
    gas, node = heapq.heappop()
    if node == end_node:
        print(gas)
        break
