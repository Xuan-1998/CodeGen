def can_make_zero(a):
    n = len(a)
    smax = sum(a)
    dp = [[False for _ in range(smax + 1)] for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        for s in range(-smax, smax + 1):
            if (s - a[i-1] >= 0) and dp[i-1][s-a[i-1]]:
                dp[i][s] = True
            elif (s + a[i-1] <= smax) and dp[i-1][s+a[i-1]]:
                dp[i][s] = True

    return "YES" if dp[n][0] else "NO"

# Example usage:
n = int(input())
a = [int(x) for _ in range(n)]
print(can_make_zero(a))
