m = int(input())
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 1
for i in range(m):
    for j in range(N, arr[i] - 1, -1):
        dp[j] += dp[j - arr[i]]
print((dp[N] % (10**9 + 7)))
