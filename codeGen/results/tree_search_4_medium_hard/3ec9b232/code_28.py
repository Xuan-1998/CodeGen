def merge_count(M):
    n = len(M)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 1

        res = 0
        for k in range(j, -1, -1):
            if M[k] <= M[j]:
                res += dp(i-1, k-1)
                break
        else:
            res = dp(i-1, j)

        memo[(i, j)] = res
        return res

    perm = {0: 1}
    for i in range(1, n):
        S = set(range(1, n+1))
        M_sorted = sorted(M[:i+1])
        for j in range(i, n-1):
            num_permutations = dp(i-1, j) * (S[j-i:].count(m) for m in M_sorted if m <= M[j]).sum()
            perm[i] = (perm.get(i-1, 0) + num_permutations) % (10**9+7)
    return perm[n-1]
