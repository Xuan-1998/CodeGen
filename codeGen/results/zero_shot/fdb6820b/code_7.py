m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(m):
    for j in range(N, -1, -1):
        if j >= sum(map(int, input().split())):
            dp[j] += dp[j - int(input())]
    print(dp[N]%10**9+7)
