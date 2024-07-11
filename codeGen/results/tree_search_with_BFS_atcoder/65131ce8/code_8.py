import sys
from operator import mul
from functools import reduce

MOD = 998244353
N = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().split()))
if D[0] != 1 or D.count(0) != 1:
    print(0)
    sys.exit()

D.sort()
C = [0]*(N+1)
C[0] = 1
for i in range(1, N+1):
    C[i] = C[i-1]*(N-i+1)*pow(i, MOD-2, MOD)%MOD

dp = [0]*N
dp[0] = 1
cnt = [0]*N
cnt[0] = 1
for i in range(1, N):
    dp[i] = dp[i-1]*cnt[D[i]-1]%MOD*C[i-1]%MOD
    cnt[D[i]] += 1

print(dp[-1])

