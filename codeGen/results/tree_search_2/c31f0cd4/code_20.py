def subsetSums(arr):
    n = len(arr)
    max_val = max(arr)
    dp = [[[] for _ in range(max_val + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_val + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (set(dp[i - 1][j]) | set([k + arr[i - 1] for k in dp[i - 1][j - arr[i - 1]]]))

    return sorted({sum(subset) for subset in dp[-1][-1]})


n = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(str, subsetSums(arr))))
