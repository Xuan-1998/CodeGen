def subsetSums(a):
    n = len(a)
    dp = [[False] * (sum(a) + 1) for _ in range(n + 1)]
    s = sum(a)

    # Base cases: sums of subsets containing or not containing the first element
    for i in range(s + 1):
        if i == 0:
            dp[0][i] = True
        elif a[0] <= i:
            dp[0][i] = dp[0][i - a[0]]
        else:
            dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(s + 1):
            if j == 0:
                dp[i][j] = True
            elif a[i] <= j:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - a[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    return [i for i in range(s + 1) if dp[n][i]]

# Example usage
a = list(map(int, input().split()))
print(' '.join(map(str, subsetSums(a))))
