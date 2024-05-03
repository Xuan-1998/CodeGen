###BEGIN CODE###
def min_replanting(n, m):
    plants = []
    for _ in range(n):
        s, x = map(int, input().split())
        plants.append((s, x))

    plants.sort(key=lambda x: x[1])
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][i] = sum(s == i - 1 for _, s in plants[:i])

    for length in range(n, m - 1, -1):
        for left in range(m - length + 1):
            right = left + length
            for current_species in set(s for _, s in plants[left:right]):
                if dp[left][left] > dp[right][right]:
                    dp[left][right] = dp[left][left]
                else:
                    dp[left][right] = min(dp[left][right], dp[left][left])

    return sum((dp[i - 1][m] - dp[i][m]) for i in range(1, m))

n, m = map(int, input().split())
print(min_replanting(n, m))
