def can_reach_end(jumps):
    n = len(jumps)
    dp = {(0, 0): 0}  # base case: starting from the first element

    for i in range(1, n):
        for r in range(n - 1, -1, -1):  # iterate over possible last reachable indices
            if r + jumps[i] >= n - 1:  # if we can reach the end with the current jump
                dp[(i, r)] = r
            else:
                dp[(i, r)] = max(dp.get((j, r - jumps[i]), 0) for j in range(i))

    return dp.get((n - 1, n - 1), False)
