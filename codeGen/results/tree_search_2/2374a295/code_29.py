def good_sequences(n, k):
    dp = {(i+1)*1000000007: 1 for i in range(2, n+1)}

    for i in range(1, n+1):
        for j in range(k-1, -1, -1):
            if (i+1) * (j+1) <= n:
                dp[(i+1)*1000000007] += dp[(i//j+1)*1000000007]

    return sum(1 for i in range(n+1) if i*1000000007 >= k)
