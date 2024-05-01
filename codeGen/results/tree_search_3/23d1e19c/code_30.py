code_block_start
n, m = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    if v in dp[:k]:
        for i in range(k - 1, -1, -1):
            if p[i] == v:
                break
        for j in range(i - 1, -1, -1):
            if dp[p[j]] > 0:
                dp[v] = max(dp[v], dp[p[j]] + 1)
                break

for i in range(1, n + 1):
    if i != t:
        for j in range(max(i - 1, 1), t + 1):
            dp[i] = min(dp[i], dp[j] + (i != j))

print(min(dp[1:]), max(dp[1:]))
code_block_end
