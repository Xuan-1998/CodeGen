def max_score(n, k, z, scores):
    dp = {(i, 0): scores[i] for i in range(1, n + 1)}
    for move_type in (1, 2):
        for i in range(z, n - k):
            if move_type == 1:
                dp[(i, move_type)] = max(dp[(i - 1, 0)], dp[(i - 1, 1)])
            else:
                dp[(i, move_type)] = max(dp[(i + 1, 2)], dp[(i - 1, 1)])
    return dp[(0, 0)]
