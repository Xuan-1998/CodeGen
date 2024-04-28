n = int(input())
nums = list(map(int, input().split()))
dp = {}
for num in nums:
    for total in range(num, sum(nums)+1):
        if total not in dp:
            dp[total] = True
        else:
            dp[total] = False
print(*sorted(dp.keys()), sep=' ')
