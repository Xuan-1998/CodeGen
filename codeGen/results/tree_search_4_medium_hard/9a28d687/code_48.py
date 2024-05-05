import sys

def solve(n, c, s):
    dp = [[0] * (max(len(x) for x in s) + 1) for _ in range(n + 1)]

    # Base cases
    dp[0][j] = 0
    dp[i][0] = -1

    for i in range(1, n + 1):
        for j in range(1, max(len(x) for x in s) + 1):
            total_cost = sys.maxsize
            for k in range(j):
                if s[i-1][k:] < s[i-2][j-k:]:  # Check lexicographical order
                    cost = dp[i-1][k] + c[i-1] + (len(s[i-1]) - k)
                    total_cost = min(total_cost, cost)

            dp[i][j] = total_cost if total_cost != sys.maxsize else -1

    return dp[n][max(len(x) for x in s)]

# Read input from stdin
n = int(input())
c = list(map(int, input().split()))
s = [input() for _ in range(n)]

print(solve(n, c, s))
