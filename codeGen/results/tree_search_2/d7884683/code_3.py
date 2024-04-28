n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n):
    left_sum = sum(arr[:i+1])
    right_sum = sum(arr[i+1:])
    if left_sum == right_sum:
        dp[i+1] = max(dp[i+1], dp[i] + 1)
    else:
        dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))
