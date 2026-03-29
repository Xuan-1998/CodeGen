def can_cross(stones):
    n = len(stones)
    dp = {(0, 0): True}
    for i in range(1, n):
        d = stones[i] - stones[i-1]
        if d < 2:
            dp[(i-1, d)] = False
        elif d == 2:
            dp[(i-1, 1)] = dp.get((i-1, 0), True) and (dp.get((i-1, 1), True) or False)
        else:
            dp[(i-1, 2)] = dp.get((i-1, 2), True) and (dp.get((i-1, 1), True) or dp.get((i-1, 0), False))
    return dp.get((n-1, stones[n-1]-stones[0]), False)
