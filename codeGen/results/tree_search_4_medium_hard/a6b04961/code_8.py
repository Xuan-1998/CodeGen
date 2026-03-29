def hedgehog_beauty(n, m):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                # Initialize the first vertex
                dp[i][j] = 0
            else:
                max_beauty = 0
                for k in range(j - 1, -1, -1):
                    if not dp[i - 1][k]:  # If the edge is not colored (i.e., it's part of the tail)
                        continue
                    # Consider extending the current tail with the new edge
                    beauty = i * (m + 1) + k
                    max_beauty = max(max_beauty, beauty)
                dp[i][j] = max_beauty

    return max(dp[n])

# Read input from stdin and process it
n, m = map(int, input().split())
print(hedgehog_beauty(n, m))
