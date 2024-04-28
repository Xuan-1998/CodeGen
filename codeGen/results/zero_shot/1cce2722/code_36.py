n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
ans = 0
for x in a:
    dp[x] += 1
for i in range(2, max(a)):
    if dp[i-1] and dp[i+1]:
        dp[i] = min(dp[i-1], dp[i+1])
ans = sum([v for v in dp[1:max(a) + 1] if not v or v % 2 == 1])
print(ans)
