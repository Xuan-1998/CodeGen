import heapq
from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [0] * (n + 1)
    parent = [-1] * (n + 1)

    pq = [(0, 0)]  # priority queue to store vertices and their earliest visit times
    while pq:
        time, vertex = heapq.heappop(pq)
        if dp[vertex] > time:
            continue

        for neighbor, weight in graph[vertex]:
            new_time = time + weight
            if dp[neighbor] <= new_time:  # already visited this vertex within the time limit
                continue
            parent[neighbor] = vertex
            dp[neighbor] = new_time
            heapq.heappush(pq, (new_time, neighbor))

    k = dp[n]
    print(k)
    for i in range(n):
        if dp[i] == k:
            print(i + 1, end=' ')
    print()

if __name__ == '__main__':
    solve()
