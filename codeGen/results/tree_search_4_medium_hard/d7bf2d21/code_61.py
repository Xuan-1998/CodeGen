dp = {}
for i in range(len(arr)):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp.get(j, 0) + 1, dp[i])
max_length = max(dp.values())
count = sum(1 for k, v in dp.items() if v == max_length)
print(count)
