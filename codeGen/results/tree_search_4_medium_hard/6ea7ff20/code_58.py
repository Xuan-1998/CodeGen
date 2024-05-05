def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(len(p) + 1)]

    for i in range(len(p)):
        if i == 0:
            dp[i][0] = (p[0] not in p[:i]) or (len(set(p[:i])) == len(p[:i]))
        else:
            dp[i][0] = False
            for j in range(n):
                if p[i] in p[:j]:
                    dp[i][0] = dp[i - 1][j] and p[i] not in p[j:]
                else:
                    dp[i][0] = dp[i - 1][j]

        for j in range(1, n + 1):
            if i == 0:
                continue
            dp[i][j] = False
            for k in range(j - 1, -1, -1):
                if p[i] in p[:k]:
                    dp[i][j] = dp[i - 1][k] and p[i] not in p[k:]
                else:
                    dp[i][j] = dp[i - 1][k]

    return "YES" if dp[-1][-1] else "NO"

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(mergeable(p))
