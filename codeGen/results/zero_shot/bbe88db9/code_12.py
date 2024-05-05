code starts here
import sys
n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (n+1)
dp[0] = 1
for i in range(1, n+1):
    if p[i-1] <= i//2:
        dp[i] += dp[i-p[i-1]]
    if i%2 == 1:
        dp[i] += dp[(i+1)//2]
    else:
        dp[i] += dp[(i-1)//2]
print(dp[n]%1000000007)
code ends here
