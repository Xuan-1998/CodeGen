n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (2*n-1) for _ in range(n)]

for i in range(n):
    dp[i][0] = 1

for i in range(1, n):
    for j in range(2*n-1):
        if i == 0:
            dp[0][j] = 1
        else:
            k = 0
            while k < 2*n-1 and (a[i] not in [a[j//2]+1, a[j//2]-1] or j//2 == 0):
                k += 1
            dp[i][j] = max(dp[i-1][k] + 1 if a[i] == a[j//2]+1 else 0 for k in range(2*n-1))

print(max(dp[-1]))
