from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s = [input() for _ in range(n)]

    dp = [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > len(t):
            return 0
        if j < 0:
            return float('inf')

        res = dp[i][j]
        for k in range(n):
            if s[k] in t[i:]:
                idx = t.index(s[k], i)
                res = min(res, dfs(idx, j - len(s[k])) + (i <= idx))
        memo[(i, j)] = res
        return res

    m = dfs(0, n)

    if m == float('inf'):
        print(-1)
    else:
        for _ in range(m):
            i, j = 0, n
            while True:
                for k in range(n):
                    if s[k] in t[i:]:
                        idx = t.index(s[k], i)
                        if idx >= i and idx <= i + len(s[k]) - 1:
                            print(k, idx - (i - 1))
                            i = idx
                            break
                j -= 1
                if j == 0:
                    break

if __name__ == "__main__":
    solve()
