# Take input
n = int(input())
a = list(map(int, input().split()))

# Initialize variables
ans = 0
dp = [1] * (n + 1)

for i in range(2, n):
    for j in range(i):
        if a[j] % (i + 1) == 0:
            dp[i + 1] += dp[j]
            dp[i + 1] %= (10**9 + 7)

ans = sum(dp)
print(ans)
