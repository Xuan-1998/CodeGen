from collections import defaultdict

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Sort strings by length
strings.sort(key=len)

dp = [[0] * (1 << n) for _ in range(n)]
for i in range(1 << n):
    dp[0][i] = 0

for i in range(n):
    for mask in range(1 << n):
        if ((mask >> i) & 1) and strings[i]:
            dp[i + 1][mask] = min(dp[i + 1][mask], dp[i][mask ^ (1 << i)] + costs[i])
        else:
            dp[i + 1][mask] = dp[i][mask]

ans = float('inf')
for mask in range(1 << n):
    if dp[-1][mask] < ans and all(s == strings[0] or s > strings[0] for s in strings):
        ans = dp[-1][mask]

print(ans) if ans != float('inf') else print(-1)
