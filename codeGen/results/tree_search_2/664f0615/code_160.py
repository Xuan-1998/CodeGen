def max_distance(v0, vf, t, delta):
    memo = {}

    def dfs(t, v):
        if (t, v) in memo:
            return memo[(t, v)]

        if t == 1:
            return min(abs(v - v0), abs(vf - v))

        res = 0
        for i in range(max(0, v0 - delta), min(vf + delta + 1)):
            res = max(res, dfs(t - 1, i) + abs(i - v))
        memo[(t, v)] = res
        return res

    return dfs(t, v0)
