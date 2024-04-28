n = int(input())
nums = list(map(int, input().split()))
dp = {}
for i in range(1 << n):
    temp = 0
    for j in range(n):
        if ((i >> j) & 1):
            temp += nums[j]
    dp.setdefault(temp, 0)
    dp[temp] += 1

print(' '.join(map(str, sorted(dp))))
