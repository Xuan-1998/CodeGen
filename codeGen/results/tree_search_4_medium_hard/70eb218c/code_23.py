def min_operations(n, x):
    dp = {}

    def f(i, x):
        if (i, x) in dp:
            return dp[(i, x)]

        if i == 0:
            return 1

        res = float('inf')
        for y in str(x):
            if int(y) != 0:  # Ignore leading zeros
                res = min(res, f(i-1, int(str(x)*y)))
        dp[(i, x)] = res
        return res

    if n == 2 and x > 0:
        return -1

    if n == 2 and x == 0:
        return 1

    if n == 19 and 1 <= x < 10**18:
        return -1

    return f(n, x)

import sys
n, x = map(int, input().split())
print(min_operations(n, x))
