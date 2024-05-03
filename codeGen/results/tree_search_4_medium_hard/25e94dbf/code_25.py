import heapq

def max_distance(commands, n):
    dp = [[0] * (n + 1) for _ in range(len(commands) + 1)]
    pq = []

    for i in range(1, len(commands) + 1):
        if commands[i - 1] == 'F':
            dp[i][0] = dp[i - 1][0] + 1
            heapq.heappush(pq, (-dp[i][0], i))
        elif commands[i - 1] == 'T':
            for j in range(min(i, n) + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
            heapq.heappush(pq, (-dp[i][n], i))
        if pq and pq[0][1] <= i:
            dist, idx = heapq.heappop(pq)
            dp[i][n] = max(dp[i][n], dp[idx][n] + int(dist))

    return -dp[-1][-1]
