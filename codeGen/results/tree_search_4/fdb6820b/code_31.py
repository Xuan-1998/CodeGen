code = '''
import sys

m, N = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[[0]*101 for _ in range(11)] for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1
for i in range(m):
    for j in range(N, arr[i]-1, -1):
        for k in range(j-arr[i], -1, -1):
            if k == 0:
                dp[j][i+1] += dp[k][i]
            else:
                dp[j][i+1] += (k < j-arr[i]) * dp[k][i]

print((dp[N][m]%10**9 + 7))
'''
