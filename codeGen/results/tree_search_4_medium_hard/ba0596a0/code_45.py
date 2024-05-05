def canCross(stones):
    n = len(stones)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        if dp[i]:
            for k in range(max(0, stones[i - 1] - 2), min(n, stones[i - 1] + 3)):
                if stones[i] - k == stones[i - 1]:
                    dp[i] = True
                    break

    return dp[-1]

# Example usage:
stones = list(map(int, input().split()))
print(canCross(stones))
