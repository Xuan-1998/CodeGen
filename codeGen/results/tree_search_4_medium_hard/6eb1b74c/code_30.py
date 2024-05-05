def solve():
    t = input().strip()
    n = int(input())
    ss = [input().strip() for _ in range(n)]

    dp = [[-1] * (len(t) + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, len(t) + 1):
        for j in range(len(ss)):
            if not any(sj in t[i-j:i] for sj in ss[:j]):
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = min(dp[k][i-1] + 1 for k in range(j)) if j > 0 else -1

    m = dp[-1][-1]

    if m == -1:
        print(-1)
    else:
        ans = []
        i, j = len(t), n
        while m > 0:
            for k in range(n):
                if dp[k][j-1] == m - 1:
                    ans.append((k, j))
                    j -= len(ss[k])
                    break
            m -= 1

        print(m)
        for a, b in sorted(ans, reverse=True):
            print(f"{a} {b}")

solve()
