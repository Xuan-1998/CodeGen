n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [0] * (n + 1)
prev_damage = [0] * n

for i in range(1, n+1):
    if prev_damage[i-1] >= h[i-1]:
        dp[i] = dp[i-1] + prev_damage[i-1]
    else:
        dp[i] = h[i-1]
    prev_damage[i-1] = max(prev_damage[i-2], h[i-1]) + 1

print(dp[-1])
