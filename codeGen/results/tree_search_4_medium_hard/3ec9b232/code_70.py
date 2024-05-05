def count_partitions(n):
    MOD = 10**9 + 7
    cache = {(0, j): 1 for j in range(n+1)}

    for i in range(1, n+1):
        for j in range(min(i, n), -1, -1):
            if j == 0:
                continue
            cache[(i, j)] = sum(cache.get((k, l-1), 0) * math.comb(i, k) for k in range(1, i+1))
            cache[(i, j)] %= MOD

    return cache[(n, n)]
