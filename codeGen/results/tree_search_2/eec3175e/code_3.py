def checkSubarraySum(arr: list[int], k: int) -> int:
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = arr[0] % k == 0

    for i in range(1, n):
        dp[i] = (dp[i - 1] or arr[i] % k == 0) and (sum(arr[:i]) % k == 0 or dp[i - 1])

    return 1 if any(dp) else 0
