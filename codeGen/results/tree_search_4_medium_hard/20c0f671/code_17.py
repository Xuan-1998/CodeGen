dp = [[float('inf')] * (max_shelf_width + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(max_shelf_width + 1):
        dp[i][w] = float('inf')
        for j in range(i):
            if books[j][0] <= w:
                dp[i][w] = min(dp[i][w], max(dp[j][k] for k in range(min(w, books[j][0]), w + 1)) + books[i - 1][1])

print(min(dp[n]))
