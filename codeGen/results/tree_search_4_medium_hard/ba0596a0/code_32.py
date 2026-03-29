def can_cross_stones(stones, k):
    n = len(stones)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i-k-1), min(n, i+k+2)):
            if abs(i-j) == k-1 or abs(i-j) == k or abs(i-j) == k+1 and dp[j]:
                dp[i] = True
                break

    return dp[-1]
