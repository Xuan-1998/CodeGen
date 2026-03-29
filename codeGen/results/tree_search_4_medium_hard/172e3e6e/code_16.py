def good_subsequences(n, a):
    MOD = 10**9 + 7

    dp = [True] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = False
        prev_len = 0
        for j in range(i):
            if a[j] % prev_len == 0 and dp[prev_len]:
                dp[i] = True
            prev_len += 1

    return sum(dp) % MOD

# Example usage:
n, *a = map(int, input().split())
print(good_subsequences(n, a))
