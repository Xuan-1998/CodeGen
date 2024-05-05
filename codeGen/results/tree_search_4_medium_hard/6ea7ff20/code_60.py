def can_merge(p):
    n = len(p) // 2

    dp = [[[True, []] for _ in range(n + 1)] for _ in range(len(p) + 1)]

    for i in range(1, len(p) + 1):
        for j in range(min(i, n) + 1):
            if p[i - 1] < p[i]:
                for k in range(j):
                    dp[i][j][0] &= (p[i - 1] not in dp[i - 1][k][1])
                    dp[i][j][0] &= (dp[i - 1][k][1] + [p[i - 1]] == p[:i])
                for k in range(j):
                    dp[i][j][0] |= (p[i - 1] not in dp[i - 1][n - k][1])
                    dp[i][j][0] &= (dp[i - 1][n - k][1] + [p[i - 1]] == p[:i])
            else:
                for k in range(j):
                    dp[i][j][0] &= (p[i - 1] not in dp[i - 1][k][1])
                    dp[i][j][0] &= (dp[i - 1][k][1] + [p[i - 1]] == p[:i])

    return "YES" if dp[-1][-1][0] else "NO"

while True:
    try:
        n = int(input())
        p = list(map(int, input().split()))
        print(can_merge(p))
    except EOFError:
        break
