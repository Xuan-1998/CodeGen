def divisible_subset(arr, m):
    memo = {}
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if i == 0: return 0
        if arr[i-1] % j == 0:
            include = dp(i-1, j - arr[i-1])
            exclude = dp(i-1, j)
            return (include or exclude) and 1
        else:
            return dp(i-1, j)
    return int(dp(len(arr), m))

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(divisible_subset(arr, m))
