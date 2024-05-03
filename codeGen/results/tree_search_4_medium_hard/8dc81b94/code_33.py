def make_equal():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 1000001 for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for k in range(max(arr[:i]) + 1):
            if arr[i - 1] == k:
                dp[i][k] = dp[i - 1][max(0, min(k - 1, 1000000))]
            elif arr[i - 1] <= k:
                dp[i][k] = dp[i - 1][min(max(0, k - arr[i - 1]), 1000000)]
            else:
                dp[i][k] = False

    print("YES" if dp[n][0] else "NO")

make_equal()
