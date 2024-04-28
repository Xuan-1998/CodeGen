import heapq

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    pq = [(float('inf'), 0)]  # priority queue: (distance from t, vertex)

    for v in path:
        while pq[0][0] > v - 1:
            _, u = heapq.heappop(pq)
        if dp[u] != 0:
            min_recomps = max(min_recomps, dp[u])
        else:
            min_recomps = 0
        dp[v] = min(max(dp[u] + 1, u in path), v not in path)

    max_recomps = max(dp[1:])
    print(f"{min_recomps} {max_recomps}")

if __name__ == "__main__":
    solve()
