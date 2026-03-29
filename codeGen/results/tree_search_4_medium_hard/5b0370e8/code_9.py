code = '''
import math

def count_ways(n, k):
    MOD = 10**9 + 7
    dp = {0: 1}

    for i in range(1, n+1):
        ways = 0
        for j in range(i-1, -1, -1):
            if (j & ((1 << k) - 1)) == (i & ((1 << k) - 1)):
                ways += dp.get(j, 0)
        dp[i] = ways % MOD

    res = 0
    for i in range(n, -1, -1):
        if (i & ((1 << k) - 1)) >= (i ^ ((1 << k) - 1)):
            res += dp.get(i, 0)
    return res % MOD

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_ways(n, k))
'''

print(code)
