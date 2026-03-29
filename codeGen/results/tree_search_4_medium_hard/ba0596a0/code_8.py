def can_cross(stones):
    n = len(stones)
    dp = [[False] * (n // 2 + 1) for _ in range(n)]

    dp[0][0] = True

    for i in range(1, n):
        for d in range(min(i - stones[i - 1], n // 2), 0, -1):
            if dp[i - 1][d]:
                if i + k <= n and abs(stones[i] - stones[i + k]) == d:
                    dp[i][d - 1] = True
                elif i + k + 1 <= n and abs(stones[i] - stones[i + k + 1]) == d:
                    dp[i][d] = True
                else:
                    dp[i][d] = True

    return dp[-1][-1]

k = int(input())
stones = list(map(int, input().split()))
print(can_cross(stones))
