from collections import defaultdict

def can_partition(n, k, m, A):
    memo = defaultdict(lambda: defaultdict(dict))

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i >= n:
            return [False]

        res = []
        for p in range(1, min(j+1, k)+1):
            diff = max(A[:i]) - min(A[:i])
            if (diff <= m and len(res) < p-1):
                res.extend(dfs(i-1, j-p))
        return [any(res)] + res

    return any(dfs(n-1, k))
