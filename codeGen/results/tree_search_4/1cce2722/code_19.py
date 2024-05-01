def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    # Initialize memoization table
    dp = {0: 0}

    for i in range(1, n):
        if a[i] not in dp:
            dp[a[i]] = dp.get(a[i] - 1, 0) + 1
        else:
            dp[a[i]] = max(dp.get(a[i] - 1, 0), dp.get(a[i] - 2, 0) + 1)

    return max(dp.values())

print(solve())
