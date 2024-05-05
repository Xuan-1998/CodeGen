def max_score(n, k, z):
    score = 0
    for i in range(k):
        if i < z:  # move to the left initially
            score += [1, n-1][i%2]  # alternate between adding 1 and n-1
        else:
            score += max([1, n-1])  # always add the maximum value after using up all allowed moves to the left

    return score
