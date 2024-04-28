n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if a[i] == a[0]:
        dp[i] = 1 + min(dp[j] for j in range(max(0, i-2), min(n, i+2)) if a[j] == a[i])
    else:
        dp[i] = n

print(min(dp))
