===BEGIN CODE===
from collections import defaultdict

def good_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = defaultdict(dict)

    for i in range(1, n+1):
        if arr[i-1] % i == 0:
            for j in range(i-1, -1, -1):
                last_divisor = min(arr[j-1], i)
                if last_divisor >= i:
                    dp[(j, last_divisor)][i] = (dp[(j, last_divisor)].get(i, 0) + 1) % (10**9+7)

    return sum(dp[(-1, -1)].values())

print(good_subsequences())
