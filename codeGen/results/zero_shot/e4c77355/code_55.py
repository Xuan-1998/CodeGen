n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], 1 + dp[j])

print(max(dp))
