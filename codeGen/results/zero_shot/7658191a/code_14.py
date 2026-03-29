def max_score(n, k, z, a):
    score = 0
    moves_made = 0
    for i in range(1, n):
        if moves_made < k and a[i] > a[i-1]:
            score += a[i]
            moves_made += 1
        elif moves_made < z:
            score -= a[i-1]
            moves_made += 1
        else:
            break
    return score
