code block
n = int(input())
nums = [int(x) for x in input().split()]

dp = [0] * (n + 1)
left = [-1] * (n + 1)

max_length = 0

for i in range(n):
    if nums[i] == 1:
        left[i + 1] = i
        dp[i + 1] = max(dp[i], 1)
    else:
        if left[i] != -1:
            max_length = max(max_length, dp[left[i]])
            left[i + 1] = -1
        dp[i + 1] = 0

print(max_length)
