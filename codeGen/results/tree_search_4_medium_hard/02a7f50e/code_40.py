import sys
from collections import defaultdict

def solve():
    n = int(input())
    dp = [[0]*n for _ in range(n)]
    memo = {}

    for i in range(1, n+1):
        pos, power = map(int, input().split())
        for j in range(i-1, -1, -1):
            state = tuple(sorted((dp[j][k] if k < j else 0 for k in range(j))))
            memo[state] = min(memo.get(state, dp[j][j]) + 1, dp[i-1][i-1])
        dp[i-1][i-1] = max(dp[i-1][i-2] if i > 1 else 0, memo.get(tuple(), dp[i-2][i-2]))

    print(memo.get(tuple(), sys.maxsize))

solve()
