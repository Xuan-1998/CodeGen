n = int(input())
nums = list(map(int, input().split()))
dp = [0] * (sum(nums) + 1)
for num in nums:
    for i in range(sum(nums), num - 1, -1):
        dp[i] += 1
print(*sorted([num for num in dp if num]), sep=' ')
