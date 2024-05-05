import sys

q = int(input())
dp = [[0] * (1 << 30) for _ in range(31)]

for u in range((1 << 30)):
    dp[0][u] = u

for k in range(1, 31):
    for u in range((1 << 30)):
        if not (u & (1 << k - 1)):
            dp[k][u] = u
        else:
            max_reachable_id = 0
            for w in range((1 << 30)):
                if (u & w) == w and dp[k - 1][w] > max_reachable_id:
                    max_reachable_id = dp[k - 1][w]
            dp[k][u] = max(dp[k - 1][u], max_reachable_id)

for _ in range(q):
    u, v = map(int, input().split())
    if dp[30][u] >= (1 << 30) - v:
        print("YES")
    else:
        print("NO")
