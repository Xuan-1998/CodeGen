import math

def min_perfect_squares(n):
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i < 0:
            return float('inf')

        if k == 0:
            return i if i >= 1 else float('inf')

        res = dp(i, k - 1)
        j = int(math.sqrt(i))
        for _j in range(j, 0, -1):
            if (_j ** 2) <= i:
                break
        for _j in range(_j, 0, -1):
            if (_j ** 2) <= i:
                res = min(res, dp(i - _j ** 2, k - 1) + 1)
                break

        memo[(i, k)] = res
        return res

    print(dp(n, n))

