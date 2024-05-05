python
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
lis = [[i]]
max_length = 1

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_length:
                max_length = dp[i]
                lis = [lis[dp.index(max(dp))]]

print(max_length)

