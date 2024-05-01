from collections import defaultdict

def max_points(a):
    n = len(a)
    dp = defaultdict(int)

    for i in range(1, n):
        dp[i] = 0
        for j in range(i):
            if a[j] == a[i]:
                dp[i] = max(dp[i], dp[j] + (i - j))

    return max(dp.values())

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
