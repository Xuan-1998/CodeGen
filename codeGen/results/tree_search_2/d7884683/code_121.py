n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i:])
    if left_sum == right_sum:
        dp[i] = max(dp[:i-1]) + 1
    else:
        dp[i] = max(dp[:i-1])

print(max(dp))
