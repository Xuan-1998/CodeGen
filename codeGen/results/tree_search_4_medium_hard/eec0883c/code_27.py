import sys
from collections import defaultdict

def solve():
    n = int(input())
    gas_stations = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    dp = [[0] * n for _ in range(n)]

    def dfs(u, parent, remaining_gas):
        if u == 0:
            return remaining_gas
        for v, capacity in graph[u]:
            if v != parent and capacity <= remaining_gas:
                remaining_gas -= capacity
                result = max(result, dfs(v, u, remaining_gas))
                remaining_gas += capacity
        return result

    print(dfs(1, -1, gas_stations[0]))

if __name__ == "__main__":
    solve()
