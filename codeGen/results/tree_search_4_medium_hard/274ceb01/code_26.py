n = int(input())
marks = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    dp[i] = min((dp[j] + (i-j)*(j+1)) for j in range(i))

print(dp[-1])
