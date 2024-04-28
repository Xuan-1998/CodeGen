n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)
max_so_far = 0

for i in range(n):
    max_so_far = max(max_so_far, arr[i])
    if max_so_far > k:
        dp[i+1] += dp[i]
    else:
        dp[i+1] = 1 if i == 0 or max_so_far > k else 0
    max_so_far = 0

print(dp[n])
