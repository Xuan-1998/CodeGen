def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * n

    dp[0] = True
    for i in range(1, n):
        for j in range(max(0, i - k - 1), min(i, k + 2)):
            if dp[j]:
                dp[i] = any(dp[j] for _ in range(k - 1, k + 2))
                break
    return dp[-1]

k = int(input())
stones = list(map(int, input().split()))
print(can_cross_stones(stones))
