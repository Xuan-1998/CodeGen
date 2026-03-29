def max_score(arr, k, z):
    n = len(arr)
    memo = [[0] * (k + 1) for _ in range(n + 1)]

    def dp(i, j):
        if i == 0:
            return 0
        if j <= 0:
            return 0

        res = max(dp(i - 1, j), dp(i - 2, min(j - 1, z)))
        if j > 0:
            res = max(res, arr[i] + dp(i - 1, j - 1))
        if i > 1 and j > 0:
            res = max(res, arr[i] + dp(i - 2, min(j - 1, z)))

        return res

    return dp(n, k)

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))
