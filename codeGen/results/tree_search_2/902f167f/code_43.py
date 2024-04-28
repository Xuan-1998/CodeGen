def dp(i, j):
    if i == m and j == n:
        return 1
    if i * j == 0:
        return float('inf')  # or some other sentinel value

    res = float('inf')
    for s in range(1, min(i, j) + 1):  # possible side lengths
        k = max(0, i - s)
        for x in range(k, min(i, j - s) + 1):
            res = min(res, dp(x, s) + dp(i - x, j - s))
    return res

n, m = map(int, input().split())
print(dp(n, m))
