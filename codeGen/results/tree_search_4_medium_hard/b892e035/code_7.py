import sys

def solve(n, probs):
    dp = [0] * (n + 1)
    seen = set()

    def dfs(i):
        if i == n:
            return 1 if len(seen) == n else 0
        p_distinct = probs[i][0]
        p_not_distinct = 1 - probs[i][0]

        if not seen.add(probs[i][1]):
            p_not_distinct *= (1 - probs[i][0])
        if not seen.add(probs[i][2]):
            p_not_distinct *= (1 - probs[i][0])

        return max(p_distinct * dfs(i - 1), p_not_distinct * dfs(i - 1))

    print(dfs(n))
