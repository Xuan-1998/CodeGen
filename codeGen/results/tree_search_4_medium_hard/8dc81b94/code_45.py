def make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False] * (10**6 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(max(arr[:i]) + 1):
            if all(a <= k for a in arr[:i]):
                dp[i][k] = True
            elif any(k - a >= 0 and dp[i-1][k-a] for a in arr[:i]):
                dp[i][k] = True

    print("YES" if dp[n][0] else "NO")

while (t := int(input())) > 0:
    make_zero()
