code
C = int(input())
for _ in range(C):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, mod[1], input().split()))
    dp = [[0] * (M + 1) for _ in range(C + 1)]
    dp[0][0] = 1
    for c in range(1, C + 1):
        for n in range(min(N, M) + 1):
            dp[c][n] = sum(dp[k][max(0, n - m)] for k in range(c, 0, -1) if k <= c and find_lower_hemisphere(k) >= m)
            dp[c][n] %= (10 ** 9 + 7)
    print(*dp[_])
