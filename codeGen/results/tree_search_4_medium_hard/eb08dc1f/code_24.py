code-block
from collections import defaultdict

def solve(n):
    dp = [0]*((10**6)+1)
    for i in range(1, n+1):
        curr_count = 0
        for l in range(min(i+1, 11), 0, -1):
            if (10**(l-1)) % (10**i) == 0:
                curr_count += dp[(10**l)-1]
        dp[i] = curr_count
    ans = []
    for i in range(1, n+1):
        ans.append((dp[i]) % 998244353)
    return ' '.join(map(str, ans))

n = int(input())
print(solve(n))
