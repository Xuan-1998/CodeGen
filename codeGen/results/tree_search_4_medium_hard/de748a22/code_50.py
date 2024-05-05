def solve():
    n, q = map(int, input().split())
    arr = list(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[j - 1] == '+' or arr[j - 1] == '-':
                dp[i][j] = (dp[i - 1][j] + 1) if arr[j - 2] != arr[j - 1] else dp[i][j]
            else:
                dp[i][j] = dp[i][j - 1]

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[l][r], (r - l + 1) // 2))

solve()
