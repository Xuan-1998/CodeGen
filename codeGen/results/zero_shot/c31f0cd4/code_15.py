n = int(input())
numbers = list(map(int, input().split()))
dp = {}
for i in range(1 << n):
    subset_sum = 0
    for j in range(n):
        if (i & (1 << j)):
            subset_sum += numbers[j]
    dp[subset_sum] = 1
max_sum = 0
for key in sorted(dp.keys()):
    max_sum = max(max_sum, key)
print(*sorted(set(range(0, max_sum+1))), sep=' ')
