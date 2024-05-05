===BEGIN CODE===
def can_cross_river(stones):
    n = len(stones)
    dp = {0: True}
    prev_jump_length = 0

    for i in range(1, n + 1):
        if stones[i] - stones[i-1] % 3 == 0:
            prev_jump_length = (stones[i] - stones[i-1]) % 3
        else:
            dp[(i-1, prev_jump_length)] or dp[(i-1, (stones[i] - stones[i-1]) % 3)]

    return dp.get((n-1, prev_jump_length), False)
===END CODE===
