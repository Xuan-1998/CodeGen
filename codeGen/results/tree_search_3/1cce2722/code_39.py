from collections import defaultdict

def delete_points(a):
    n = len(a)
    dp = [[0] * 106 for _ in range(n+1)]

    for i in range(1, n+1):
        for k in range(1, 106):
            if a[i-1] == k:
                dp[i][k] = max(dp[i-1][k-1], dp[i-1][k+1]) if i > 1 else 0
            else:
                dp[i][k] = dp[i-1][k]

    return max(max(row) for row in dp)

n = int(input())
a = list(map(int, input().split()))
print(delete_points(a))
