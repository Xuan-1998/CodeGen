def findDistinctSums(A):
    n = len(A)
    A.sort()
    dp = {0: set()}
    total_sum = sum(A)

    for i, num in enumerate(A):
        for j in range(total_sum, num - 1, -1):
            if j - num not in dp.get(j - 2 * num, {}):
                if j - num not in dp:
                    dp[j] = set()
                dp[j].update(dp.get(j - num, {}))
                dp[j].add(j)
        for i in range(len(A), 0, -1):
            dp[total_sum - A[i-1]].add(total_sum - A[i-1])
    res = []
    for k in sorted(dp.keys()):
        res.extend(sorted(list(dp[k])))
    return ' '.join(map(str, res))
