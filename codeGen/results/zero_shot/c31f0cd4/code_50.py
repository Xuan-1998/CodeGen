n = int(input())
nums = list(map(int, input().split()))
dp = [[num] for num in nums]
sums = set()

for i in range(1, n):
    for j in range(i):
        for k in range(len(dp[j])):
            new_sum = sum(dp[j][k]) + nums[i]
            if new_sum not in sums:
                dp.append([new_sum])
                sums.add(new_sum)

print(*sorted(list(sums)), sep=' ')
