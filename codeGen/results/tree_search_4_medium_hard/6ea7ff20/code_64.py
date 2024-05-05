def solve():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[False] * (n + 1) for _ in range(2 * n + 1)]

    # Base case: when i = 0, dp[0][k] = true for all k
    for k in range(n + 1):
        dp[0][k] = True

    for i in range(1, 2 * n + 1):
        for j in range(min(i, n), -1, -1):
            if p[i-1] < p[j-1]:
                for k in range(j-1, -1, -1):
                    dp[i][j] = dp[i][k] and True
            elif p[i-1] >= p[j-1]:
                for k in range(j, n+1):
                    dp[i][j] = dp[i][k] and True

    ans = False
    for i in range(n + 1, 2 * n + 1):
        for j in range(max(0, i-n), -1, -1):
            if dp[i][j]:
                ans = True
                break

    print("YES" if ans else "NO")

solve()
