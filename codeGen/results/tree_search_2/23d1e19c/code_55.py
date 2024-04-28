import heapq

def min_max_recomputations():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    # Initialize DP table and priority queue
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    pq = []

    # Build priority queue with initial values
    for i in range(1, n + 1):
        heapq.heappush(pq, (0, i))  # (dist, vertex)

    # Compute shortest distances and update DP table
    for _ in range(k):
        dist, v = heapq.heappop(pq)
        if dp[v][_] < float('inf'):
            continue

        for u, _ in edges:
            if u == v:  # Directed edge from u to v
                new_dist = dist + 1
                if dp[u][_ + 1] > new_dist:
                    dp[u][_ + 1] = new_dist
                if dp[u][_] < new_dist:
                    dp[u][_] = new_dist

        heapq.heappush(pq, (new_dist, v))  # Update priority queue

    # Compute minimum and maximum recomputations needed
    min_recomputations = min(dp[-1])
    max_recomputations = max(dp[-1])

    print(min_recomputations, max_recomputations)

if __name__ == "__main__":
    min_max_recomputations()
