def min_cuts(s):
    n = len(s)
    dp = [n] * (n + 1)
    for i in range(n + 1):
        left, right = 0, i
        while left <= right:
            if s[left:right+1] == s[left:right+1][::-1]:
                dp[i] = min(dp[i], dp[left-1] if left > 0 else 0)
                left += 1
                right -= 1
            else:
                dp[i] = min(dp[i], dp[left-1] if left > 0 else n, dp[right+1] if right < n - 1 else n) + 1
                break
    return dp[-1]
