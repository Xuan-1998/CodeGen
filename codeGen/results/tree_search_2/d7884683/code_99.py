n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i:])
    for j in range(i - 1, -1, -1):
        if left_sum == right_sum:
            dp[i] = max(dp[i], dp[j] + 1)
    dp[i] = max(dp[i], 0)

print(max(dp))
