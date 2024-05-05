import math

mod = 998244353

def dp(i, k):
    if i == 0:
        return 1
    elif k == 0:
        return 1
    else:
        ways = 0
        for j in range(k+1):
            if (j + 1) <= i:
                ways += dp(j, k-1)
        return ways % mod

n = int(input())
for _ in range(n):
    i, k = map(int, input().split())
    print(dp(i, k))
