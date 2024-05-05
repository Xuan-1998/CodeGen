input_array = list(map(int, input().split()))
n = len(input_array)
dp = [[1]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if input_array[j] > input_array[i-1]:
            for k in range(i):
                if input_array[j] > input_array[k]:
                    dp[i][j] = max(dp[i][j], 1 + dp[k][i-1])

print(max(dp[-1]))
