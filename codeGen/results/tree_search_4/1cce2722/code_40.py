import sys
from collections import defaultdict

def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)
    memo = defaultdict(int)

    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            if a[j] == a[i-1]:
                dp[i] = max(dp[i], dp[j] + (i-j))
            else:
                dp[i] = max(dp[i], dp[j])
        memo[a[i-1]] = i

    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(a))
