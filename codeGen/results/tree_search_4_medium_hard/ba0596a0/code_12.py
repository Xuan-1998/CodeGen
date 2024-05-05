def canCross(stones):
    dp = {(0, k): True for k in range(1, max(stones) + 2)}

    for i in range(len(stones)):
        for j in range(1, min(i + 3, len(stones)) + 1):
            if stones[i] - stones[i-j] >= j-1 and stones[i] - stones[i-j] <= j+1:
                dp[(i, j)] = max(dp.get((i-1, j-1), False) or (i-j)%3==0, 
                                 dp.get((i-1, j), False) or (i-j-1)%3==0)
    return bool(dp.popitem()[1])

