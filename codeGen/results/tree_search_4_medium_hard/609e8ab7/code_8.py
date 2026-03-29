import heapq

def solve():
    n = int(input())
    
    edges = list(map(int, input().split()))
    ranges = []
    for _ in range(n-1):
        l, r = map(int, input().split())
        ranges.append((l, r))

    dp = [(0, None)] * (n+1)
    pq = [(0, 0)]

    while pq:
        val, node = heapq.heappop(pq)

        if dp[node][0] != val:
            continue

        for child in range(node+1, n):
            if edges[child-1] == node:
                new_val = val + (ranges[child-1][1] - ranges[child-1][0])
                parent = edges[child-1]
                heapq.heappush(pq, (new_val, child))
                dp[child] = (new_val, parent)
            else:
                continue

    print(dp[1][0])

solve()
