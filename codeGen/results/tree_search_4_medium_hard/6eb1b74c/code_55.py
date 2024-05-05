from collections import defaultdict

def solve(t, s):
    n = len(t)
    m = len(s)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    last_used = [-1 for _ in range(m+1)]

    def dfs(pos, substrings):
        if pos > n or not substrings:
            return 0

        if dp[pos][len(substrings)] != -1:
            return dp[pos][len(substrings)]

        res = float('inf')
        for i, substring in enumerate(substrings):
            if t.find(substring) == pos:
                new_substrings = substrings[:i] + substrings[i+1:]
                res = min(res, dfs(pos+len(substring), new_substrings) + 1)
                last_used[len(substrings)] = i
        dp[pos][len(substrings)] = res if res != float('inf') else -1
        return res

    steps = dfs(0, list(range(m)))
    if steps == -1:
        print(-1)
    else:
        for j in range(steps):
            print(last_used[j+1], j*len(s[j]))
