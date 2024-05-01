def solve(s, t, path):
    n = len(path)
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    def f(v, d):
        if v == t:
            return 0, 0
        if dp[v][d] != float('inf'):
            return dp[v][d]
        min_rec, max_rec = float('inf'), 0
        for p in path[:path.index(v) + 1]:
            if d < dp[p][dp[p].index(t)]:
                rec_min, rec_max = f(p, dp[p].index(t))
                rec_min += 1
                rec_max += 1
                min_rec = min(min_rec, rec_min)
                max_rec = max(max_rec, rec_max)
        dp[v][d] = (min_rec, max_rec)
        return dp[v][d]

    for v in range(s, t + 1):
        if v != t:
            rec_min, rec_max = f(v, path.index(v))
            rec_min += 1
            rec_max += 1
            dp[path.index(v)][0] = (rec_min, rec_max)

    return dp[path.index(t)][0]

# Example usage:
s = 1
t = 5
path = [1, 2, 3, 4, 5]
print(solve(s, t, path))  # Output: (1, 2)
