n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
ans = 0
for x in a:
    dp[x] += 1
for i in range(1, max(a) + 1):
    ans += dp[i]
print(ans)
