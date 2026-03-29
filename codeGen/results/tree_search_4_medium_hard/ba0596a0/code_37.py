def canCross(stones):
    n = len(stones)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n):
        if dp[i]:
            for k in range(max(1, stones[i] - 2), min(n, stones[i] + 3)):
                if k not in stones:
                    dp[k] = True

    return dp[-1]

# Test your function
stones = [0, 2, 5, 6, 7]
print(canCross(stones))  # Output: True
