import sys

def solve(n, k):
    s = input().strip()
    dp = [False] * (k + 1)
    dp[0] = True

    memo = {}

    def dfs(j):
        if j < 0:
            raise ValueError("Invalid length")
        if j == 0:
            return s[0]
        if j not in memo:
            memo[j] = False
            for i in range(1, n + 1):
                if j - i >= 0 and not dp[j - i]:
                    continue
                if s[i - 1] <= s[0]:
                    memo[j] = s[:i]
                    break
                else:
                    memo[j] = s[:i - 1]
        return memo[j]

    for _ in range(k):
        j = k - _
        result = dfs(j)
        print(result, end="")
