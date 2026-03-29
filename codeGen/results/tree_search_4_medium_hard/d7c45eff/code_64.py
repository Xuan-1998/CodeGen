import sys
from collections import defaultdict

def smallest_string(n, k):
    dp = [[[] for _ in range(26)] for _ in range(n+1)]
    memo = {}

    def dfs(i, j, prefix_length):
        if (i, j, prefix_length) in memo:
            return memo[(i, j, prefix_length)]

        if i == 0 or j == -1:
            return [''] * k

        ans = []
        for s in dp[i-1][j]:
            ans.extend([s] * (k - len(s)))
            for t in dfs(i-1, j-1, prefix_length-1):
                ans.append(s + t)
        if i <= k and not ans:
            ans.append('a' * (i - 1))
        return ans

    res = []
    for s in dfs(n, ord('z') - ord('a'), n):
        res.extend([s] * (k // len(s) + 1))
    res.sort()
    return ''.join(res[:k])

n, k = map(int, input().split())
print(smallest_string(n, k))
