def shortestUncommonSubsequence(S, T):
    m, n = len(S), len(T)

    if m == 0 and n == 0:
        return 0

    if m == 0:
        return n

    if n == 0:
        return m

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # ... (rest of the code remains the same)
