def min_squares(n, m):
    dp = {(i, j): float('inf') for i in range(n+1) for j in range(m+1)}
    dp[(0, 0)] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i >= j and j > 0:
                dp[(i, j)] = min(dp[(i-j, j)], dp[(i, j-j)]) + 1
            elif i > 0:
                dp[(i, j)] = min(dp[(i-1, j)], dp[(i, j-1)]) + 1

    return dp[(n, m)]

import sys

n, m = map(int, input().split())
print(min_squares(n, m))
